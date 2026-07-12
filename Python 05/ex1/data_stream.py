from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._internal_data: list[str] = []
        self._consumed_index: int = -1
        self._ingested_counter: int = 0
        self._consumed_counter: int = 0

    def get_ingested(self) -> int:
        return self._ingested_counter

    def get_remaining(self) -> int:
        return self._ingested_counter - self._consumed_counter

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        if isinstance(data, list):
            self._ingested_counter += len(data)
        else:
            self._ingested_counter += 1

    def output(self) -> tuple[int, str]:
        if not self._internal_data:
            raise IndexError("Ingest more data to be consumed.")
        self._consumed_index += 1
        self._consumed_counter += 1
        oldest_item = self._internal_data.pop(0)
        return self._consumed_index, oldest_item


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        def _validate_numbers(data: Any) -> bool:
            if type(data) in (int, float):
                return True
            return False

        if type(data) in (int, float):
            return True
        elif type(data) is list:
            if (len(data) == 0):
                return False
            return all(_validate_numbers(_) for _ in data)
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Data must be int, float or list[int | float]")

        if type(data) in (int, float):
            self._internal_data.append(str(data))
        elif type(data) is list:
            self._internal_data.extend([str(value) for value in data])

        super().ingest(data)


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if type(data) is (str):
            return True

        if type(data) is (list):
            if (len(data) == 0):
                return False
            return all(type(_) is str for _ in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Data must be str or list[str]")

        if isinstance(data, str):
            self._internal_data.append(data)
        elif isinstance(data, list):
            self._internal_data.extend([str(value) for value in data])

        super().ingest(data)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        def _validate_dict(data: Any) -> bool:
            if type(data) is not dict:
                return False

            if (len(data) == 0):
                return False
            return all(type(k) is str and type(v) is str
                       for k, v in data.items())

        if type(data) not in (dict, list):
            return False

        if type(data) is dict:
            return _validate_dict(data)

        else:
            if (len(data) == 0):
                return False
            return all(_validate_dict(_) for _ in data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Data must be a dict of string key-value pairs")

        if isinstance(data, list):
            for value in data:
                self._internal_data.extend([f"'{str(k)}': '{str(v)}'"
                                            for k, v in value.items()])

        elif (isinstance(data, dict)):
            self._internal_data.extend([f"'{str(k)}': '{str(v)}'"
                                        for k, v in data.items()])

        super().ingest(data)


class DataStream():

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            raise TypeError("The proc must inherit from Dataprocessor")

        for process in self._processors:
            if type(process) is type(proc):
                print(f"Already exists a process type {type(proc).__name__}.")
                return

        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for value in stream:
            is_processed = False

            for process in self._processors:
                try:
                    process.ingest(value)
                    is_processed = True
                    break
                except TypeError:
                    continue

            if not is_processed:
                print("DataStream error - Can't process element in stream: "
                      f"{value}")

    def print_processors_stats(self) -> None:
        if len(self._processors) == 0:
            print("No processor found, no data")
            return

        for process in self._processors:
            type_name = type(process).__name__
            remaining = process.get_remaining()
            ingested = process.get_ingested()
            print(f"{type_name}: total {ingested} items processed, "
                  f"remaining {remaining} on processor")


def main() -> None:

    numeric: NumericProcessor = NumericProcessor()
    text: TextProcessor = TextProcessor()
    log: LogProcessor = LogProcessor()
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    stream = DataStream()

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("Registering Numeric Processor\n")
    stream.register_processor(numeric)

    batch_data = ['Hello world', [3.14, -1, 2.71],
                  [{'log_level': 'WARNING',
                    'log_message': 'Telnet access! Use ssh instead'},
                   {'log_level': 'INFO',
                    'log_message': 'User wil isconnected'}],
                  42, ['Hi', 'five']]

    print(f"Send first batch of data on stream: {batch_data}\n")
    stream.process_stream(batch_data)

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print("Registering other data processors")
    stream.register_processor(text)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(batch_data)

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()

    print("== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()

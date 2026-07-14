from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._internal_data: list[str] = []
        self._consumed_index: int = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._internal_data:
            raise IndexError("Ingest more data to be consumed.")
        self._consumed_index += 1
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


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        def _validate_dict(data: Any) -> bool:
            if type(data) is not dict:
                return False

            if (len(data) != 2):
                return False

            if "log_level" in data and "log_message" in data:
                keys = list(data.keys())
                if keys.index("log_level") > keys.index("log_message"):
                    return False
            else:
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
        def _ingest_dict(data) -> None:
            self._internal_data.append(f"{data['log_level']}: "
                                       f"{data['log_message']}")

        if not self.validate(data):
            raise TypeError("Data must be a dict of string key-value pairs."
                            "Usage: {log_level: <level>, log_message: <msg>}")

        if isinstance(data, list):
            for value in data:
                _ingest_dict(value)
        elif (isinstance(data, dict)):
            _ingest_dict(data)


def test_behavior(instance: DataProcessor, data: list[Any]) -> None:
    print(f"Data used to make testing: '{data}'")
    print("\n---Testing validate method---")
    for value in data:
        print(f"Trying to validate input {value}: {instance.validate(value)}")

    print("\n---Testing ingest method---")
    for value in data:
        try:
            instance.ingest(value)
        except Exception as ex:
            print(f"Got exception with ingestion of {value}: {ex}")

    print("\n---Testing output method---")
    while True:
        try:
            index, value = instance.output()
            print(f"Value {index}: {value}")
        except IndexError as ex:
            print(ex)
            break


def main() -> None:

    numeric: NumericProcessor = NumericProcessor()
    text: TextProcessor = TextProcessor()
    log: LogProcessor = LogProcessor()
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...\n")
    test_behavior(numeric, [42, '42', 42.42, [1, 2, 3],
                            [42.42, 123, 0, 'abc'], 'Hello'])
    print("Testing Text Processor...\n")
    test_behavior(text, [42, 'Hello', 'Nexus', 'World', ['List', 'Prove'],
                         [{'dict': 'prove'}], [], {}])
    print("Testing Log Processor...\n")
    test_behavior(log, [[{'log_level': 'NOTICE',
                          'log_message': 'Connection to server'},
                        {'log_level': 'ERROR',
                         'log_message': 'Unauthorized access!!'}],
                        {'log_level': 'INFO'}, {}, {'log_level': 1},
                        {'log_message': 'Test', 'log_level': 'ERROR'},
                        "prueba", 123])


if __name__ == "__main__":
    main()

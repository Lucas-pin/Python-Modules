from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self):
        self._internal_data = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        pass


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        
        def _validate_numbers(data: Any) -> bool:
            if type(data) in (int, float):
                return True

        if type(data) is list:
            if (len(data) == 0):
                return False
            return all(_validate_numbers(_) for _ in data)
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        try:
            if type(data) in (int, float):
                    self._internal_data.append(str(data))
            elif type(data) is list:
                self._internal_data.extend([str(value) for value in data])
            else:
                raise TypeError("Data must be int, float or list[int | float]")
        except Exception as ex:
            print("Data cannot be converted to a string")
            raise ValueError("Ingest data failed") from ex
        
        



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
        try:
            if isinstance(data, str):
                    self._internal_data.append(data)
            elif isinstance(data, list):
                self._internal_data.extend([str(value) for value in data])
            else:
                raise TypeError("Data must be str or list[str]")
        except Exception as ex:
            raise ValueError("Ingest data failed") from ex


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        def _validate_dict(data: Any) -> bool:
            if type(data) is not dict:
                return False

            if (len(data) == 0):
                return False
            return all(type(k) is str and type(v) is str for k, v in data.items())

        if type(data) not in (dict, list):
            return False

        if type(data) is dict:
            return _validate_dict(data)
        
        else:
            if (len(data) == 0):
                return False
            return all(_validate_dict(_) for _ in data)
    
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        pass
#!/usr/bin/python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        super().__init__()
        self.queue = {}

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # Outputs ingested data
    def output(self) -> tuple[int, str]:
        rank, number = list(self.queue.items())[0]
        self.queue.pop(rank)
        return (rank, number)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float, list)):
            if isinstance(data, list):
                is_valid = all(isinstance(x, (int, float)) for x in data)
                return is_valid
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError(f"Invalid data type: '{data}' is {type(data)}, "
                            "expected (<int> | <float> | <list[int | float]>)")
        print(f"Processing data: {data}")
        for rank, number in zip(range(len(data)), data):
            self.queue[rank] = number


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (str, list)):
            if isinstance(data, list):
                is_valid = all(isinstance(x, str) for x in data)
                return is_valid
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError(f"Invalid data type: '{data}' is {type(data)}, "
                            "expected <str>")
        print(f"Processing data: {data}")
        for rank, text in zip(range(len(data)), data):
            self.queue[rank] = text


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        valid = False
        if isinstance(data, dict):
            valid = self.is_valid(data)
        elif isinstance(data, list):
            valid = all(self.is_valid(dictionary) for dictionary in data)
        return valid

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError(f"Invalid data type: '{data}' is {type(data)}, "
                            "expected (<dict>, <list[dict]>)")
        print(f"Processing data: {data}")
        for rank, log in zip(range(len(data)), data):
            self.queue[rank] = f"{log['log_level']}: {log['log_message']}"

    def is_valid(self, data: dict) -> bool:
        return all(isinstance(key, str) and
                   isinstance(value, str) for key, value in data.items())


def main():
    numProcessor = NumericProcessor()
    textProcessor = TextProcessor()
    logProcessor = LogProcessor()
    print("=== Code Nexus - Data Processor ===")

    # Testing Numeric Processor
    print("\nTesting Numeric Processor...")
    print(f"Trying to validate input '42': {numProcessor.validate(42)}")
    print("Trying to validate input 'Hello': "
          f"{numProcessor.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numProcessor.ingest("foo")
    except TypeError as err:
        print(err)
    numProcessor.validate([1, 2, 3, 4, 5])
    numProcessor.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, number = numProcessor.output()
        print(f"Numeric value {rank}: {number}")

    # Testing Text Processor
    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {textProcessor.validate(42)}")
    textProcessor.validate(['Hello', 'Nexus', 'World'])
    textProcessor.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, text = textProcessor.output()
        print(f"Text value {rank}: {text}")

    # Testing Log Processor
    print("\nTesting Log Processor...")
    print(f"Trying to validate input 'Hello': "
          f"{logProcessor.validate('Hello')}")
    logProcessor.validate([{'log_level': 'NOTICE',
                            'log_message': 'Connection to server'},
                           {'log_level': 'ERROR',
                            'log_message': 'Unauthorized access!!'}])
    logProcessor.ingest([{'log_level': 'NOTICE',
                          'log_message': 'Connection to server'},
                         {'log_level': 'ERROR',
                          'log_message': 'Unauthorized access!!'}])
    print("Extracting 2 values...")
    for _ in range(2):
        rank, log = logProcessor.output()
        print(f"Log entry {rank}: {log}")


if __name__ == "__main__":
    main()

#!/usr/bin/python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.queue: dict[int, Any] = {}
        self.id: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # Outputs ingested data
    def output(self) -> tuple[int, str]:
        if not self.queue:
            raise ValueError("no processes remaining!")
        oldest = min(self.queue.keys())
        value = self.queue.pop(oldest)
        return (oldest, value)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float, list)):
            if isinstance(data, list):
                return all(isinstance(x, (int, float)) for x in data)
            else:
                return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        print(f"Processing data: {data}")
        if isinstance(data, list):
            for value in data:
                self.queue[self.id] = str(value)
                self.id += 1
        else:
            self.queue[self.id] = str(data)
            self.id += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (str, list)):
            if isinstance(data, list):
                is_valid = all(isinstance(x, str) for x in data)
                return is_valid
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        print(f"Processing data: {data}")
        if isinstance(data, list):
            for text in data:
                self.queue[self.id] = text
                self.id += 1
        else:
            self.queue[self.id] = data
            self.id += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        valid = False
        if isinstance(data, dict):
            valid = self.is_valid(data)
        elif isinstance(data, list):
            valid = all(self.is_valid(item) for item in data)
        return valid

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        print(f"Processing data: {data}")
        if isinstance(data, list):
            for log in data:
                output = f"{log['log_level']}: {log['log_message']}"
                self.queue[self.id] = output
                self.id += 1
        else:
            self.queue[self.id] = f"{data['log_level']}: {data['log_message']}"
            self.id += 1

    def is_valid(self, data: dict[str, str]) -> bool:
        return all(isinstance(key, str) and
                   isinstance(value, str) for key, value in data.items())


def main() -> None:
    numProcessor = NumericProcessor()
    textProcessor = TextProcessor()
    logProcessor = LogProcessor()
    basic_dict = {'log_level': 'Test', 'log_message': 'Testing'}
    tests = [7, 3.14, "foo", {"log_level": "TEST",
                              "log_message": "TESTING: Test purposes text"}]
    ident_level_1 = "   "
    ident_level_2 = "      "
    print("=== Code Nexus - Data Processor ===")

    # Testing Numeric Processor
    print("\n==Testing Numeric Processor...")
    print(f"{ident_level_1}=Validations tests")
    print(f"{ident_level_2}Trying to validate input '42': "
          f"{numProcessor.validate(42)}")
    print(f"{ident_level_2}Trying to validate input 'Hello': "
          f"{numProcessor.validate('Hello')}")
    print(f"{ident_level_2}Trying to validate input '{basic_dict}': "
          f"{numProcessor.validate(basic_dict)}")
    print(f"{ident_level_1}=Test ingestions without prior validation for "
          f"{tests}:")
    for test in tests:
        try:
            if isinstance(test, int | float):
                print(f"{ident_level_2}", end='')
            numProcessor.ingest(test)
            numProcessor.output()
        except ValueError as err:
            print(f"{ident_level_2}Got exception with '{test}': {err}")
    print(f"{ident_level_1}=Validation and Ingestion of valid inputs:")
    try:
        print(f"{ident_level_2}", end='')
        numProcessor.validate([1, 2, 3, 4, 5])
        numProcessor.ingest([1, 2, 3, 4, 5])
    except ValueError as err:
        print(f"{ident_level_2}Got exception: {err}")
    print(f"{ident_level_1}=Extracting 3 values...")
    try:
        for _ in range(3):
            rank, number = numProcessor.output()
            print(f"{ident_level_2}Numeric value {rank}: {number}")
    except ValueError as err:
        print(f"{ident_level_2}Got exception: {err}")

    # Testing Text Processor
    print("\n==Testing Text Processor...")
    print(f"{ident_level_1}=Validations tests")
    print(f"{ident_level_2}Trying to validate input '42': "
          f"{textProcessor.validate(42)}")
    print(f"{ident_level_2}Trying to validate input 'Hello': "
          f"{textProcessor.validate('Hello')}")
    print(f"{ident_level_2}Trying to validate input '{basic_dict}': "
          f"{textProcessor.validate(basic_dict)}")
    print(f"{ident_level_1}=Test ingestions without prior validation for "
          f"{tests}:")
    for test in tests:
        try:
            if isinstance(test, str):
                print(f"{ident_level_2}", end='')
            textProcessor.ingest(test)
            textProcessor.output()
        except ValueError as err:
            print(f"{ident_level_2}Got exception with '{test}': {err}")
    print(f"{ident_level_1}=Validation and Ingestion of valid inputs:")
    try:
        print(f"{ident_level_2}", end='')
        textProcessor.validate(['Hello', 'Nexus', 'World'])
        textProcessor.ingest(['Hello', 'Nexus', 'World'])
    except ValueError as err:
        print(f"{ident_level_2}Got exception: {err}")
    print(f"{ident_level_1}=Extracting 3 values...")
    try:
        for _ in range(3):
            rank, text = textProcessor.output()
            print(f"        Text value {rank}: {text}")
    except ValueError as err:
        print(f"{ident_level_2}Got exception: {err}")

    # Testing Log Processor
    print("\n==Testing Log Processor...")
    print(f"{ident_level_1}=Validations tests")
    print(f"{ident_level_2}Trying to validate input 42: "
          f"{logProcessor.validate(42)}")
    print(f"{ident_level_2}Trying to validate input 'Hello': "
          f"{logProcessor.validate('Hello')}")
    print(f"{ident_level_2}Trying to validate input '{basic_dict}': "
          f"{logProcessor.validate(basic_dict)}")
    print(f"{ident_level_1}=Test ingestions without prior validation for "
          f"{tests}:")
    for test in tests:
        try:
            if isinstance(test, dict):
                print(f"{ident_level_2}", end='')
            logProcessor.ingest(test)
            logProcessor.output()
        except (ValueError, KeyError) as err:
            print(f"{ident_level_2}Got exception with '{test}': {err}")
    print(f"{ident_level_1}=Validation and Ingestion of valid inputs:")
    try:
        print(f"{ident_level_2}", end='')
        logProcessor.validate([{'log_level': 'NOTICE',
                                'log_message': 'Connection to server'},
                               {'log_level': 'ERROR',
                                'log_message': 'Unauthorized access!!'}])
        logProcessor.ingest([{'log_level': 'NOTICE',
                              'log_message': 'Connection to server'},
                             {'log_level': 'ERROR',
                              'log_message': 'Unauthorized access!!'}])
    except ValueError as err:
        print(f"Got exception: {err}")
    print(f"{ident_level_1}=Extracting 2 values...")
    try:
        for _ in range(2):
            rank, log = logProcessor.output()
            print(f"{ident_level_2}Log entry {rank}: {log}")
    except ValueError as err:
        print(f"{ident_level_2}Got exception: {err}")


if __name__ == "__main__":
    main()

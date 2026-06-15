#!/usr/bin/python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.queue: dict[int, Any] = {}
        self.processed: int = 0
        self.remaining: int = 0
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
        self.remaining -= 1
        return (oldest, value)

    def register_process(self, data: str) -> None:
        self.queue[self.id] = data
        self.id += 1
        self.processed += 1
        self.remaining += 1


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
        if isinstance(data, list):
            for value in data:
                # self.queue[self.id] = str(value)
                # self.id += 1
                self.register_process(str(value))
        else:
            # self.queue[self.id] = str(data)
            # self.id += 1
            self.register_process(str(data))


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
        if isinstance(data, list):
            for text in data:
                # self.queue[self.id] = text
                # self.id += 1
                self.register_process(str(text))
        else:
            # self.queue[self.id] = data
            # self.id += 1
            self.register_process(str(data))


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
        if isinstance(data, list):
            for log in data:
                output = f"{log['log_level']}: {log['log_message']}"
                # self.queue[self.id] = output
                # self.id += 1
                self.register_process(output)
        else:
            output = f"{data['log_level']}: {data['log_message']}"
            # self.queue[self.id] = output
            # self.id += 1
            self.register_process(output)

    def is_valid(self, data: dict[str, str]) -> bool:
        return all(isinstance(key, str) and
                   isinstance(value, str) for key, value in data.items())


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if type(proc) in [type(processor) for processor in self.processors]:
            pass
        else:
            self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processor_selected = None
            try:
                for processor in self.processors:
                    if processor.validate(element):
                        processor.ingest(element)
                        processor_selected = processor
                        break
                if not processor_selected:
                    raise TypeError("DataStream error - Can't process "
                                    f"element in stream: {element}")
            except TypeError as err:
                print(err)

    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        if len(self.processors) == 0:
            print("No processor found, no data")
        else:
            for processor in self.processors:
                print(f"{processor.__class__.__name__}: total "
                      f"{processor.processed} items processed, remaining "
                      f"{processor.remaining} on processor")
        print()


def main() -> None:

    def run_task(proc: DataProcessor, cycles: int) -> None:
        try:
            for _ in range(cycles):
                proc.output()
        except ValueError as err:
            print(f"Error in '{proc.__class__.__name__}': {err}")

    numProcessor = NumericProcessor()
    textProcessor = TextProcessor()
    logProcessor = LogProcessor()
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    d_stream = DataStream()
    d_stream.print_processors_stats()

    print("Registering Numeric Processor\n")
    d_stream.register_processor(numProcessor)

    stream = ['Hello world', [3.14, -1, 2.71],
              [{'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'},
               {'log_level': 'INFO',
                'log_message': 'User wil is connected'}],
              42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {stream}")
    d_stream.process_stream(stream)
    d_stream.print_processors_stats()

    print("Registering other data processors")
    d_stream.register_processor(textProcessor)
    d_stream.register_processor(logProcessor)
    print("Send the same batch again")
    d_stream.process_stream(stream)
    d_stream.print_processors_stats()

    print("Consume some elements from the data processors: Numeric 3, "
          "Text 2, Log 1")
    run_task(numProcessor, 3)
    run_task(textProcessor, 2)
    run_task(logProcessor, 1)
    d_stream.print_processors_stats()


if __name__ == "__main__":
    main()

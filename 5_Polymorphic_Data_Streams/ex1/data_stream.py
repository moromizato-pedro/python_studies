#!/usr/bin/python3

import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self):
        super().__init__()
        self.queue = {}
        self.processed = 0
        self.remaining = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    # Outputs ingested data
    def output(self) -> tuple[int, str]:
        rank, number = list(self.queue.items())[0]
        self.queue.pop(rank)
        self.remaining -= 1
        return (rank, number)

    def register_process(self, data: typing.Any, rank: int=0) -> None:
        self.queue[rank] = data
        self.processed += 1
        self.remaining += 1


class DataStream():
    def __init__(self):
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        if proc in self.processors:
            pass
        else:
            self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            processor_selected = None
            try:
                for processor in self.processors:
                    if processor.validate(element):
                        processor.ingest(element)
                        processor_selected = processor
                        break
                if not processor_selected:
                    raise TypeError(f"DataStream error - Can't process element in stream: {element}")
            except TypeError as err:
                print(err)

    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        if len(self.processors) == 0:
            print("No processor found, no data")
        else:
            for processor in self.processors:
                print(f"{processor.__class__.__name__}: total {processor.processed} items processed, remaining {processor.remaining} on processor")
        print()


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        is_valid = True
        if isinstance(data, (int, float, list)):
            if isinstance(data, list):
                is_valid = all(isinstance(x, (int, float)) for x in data)
            return is_valid
        else:
            return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise TypeError(f"Invalid data type: '{data}' is {type(data)}, "
                            "expected (<int> | <float> | <list[int | float]>)")
        # print(f"Processing data: {data}")
        if isinstance(data, list):
            for rank, number in zip(range(len(data)), data):
                self.register_process(number, rank)
        else:
            self.register_process(data)


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        is_valid = True
        if isinstance(data, (str, list)):
            if isinstance(data, list):
                is_valid = all(isinstance(x, str) for x in data)
            return is_valid
        else:
            return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise TypeError(f"Invalid data type: '{data}' is {type(data)}, "
                            "expected <str>")
        # print(f"Processing data: {data}")
        if isinstance(data, list):
            for rank, text in zip(range(len(data)), data):
                self.register_process(text, rank)
        else:
            self.register_process(data)


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        valid = False
        if isinstance(data, dict):
            valid = self.is_valid(data)
        elif isinstance(data, list):
            valid = all(self.is_valid(dictionary) for dictionary in data)
        return valid

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise TypeError(f"Invalid data type: '{data}' is {type(data)}, "
                            "expected (<dict>, <list[dict]>)")
        # print(f"Processing data: {data}")
        # for rank, log in zip(range(len(data)), data):
        #     self.queue[rank] = f"{log['log_level']}: {log['log_message']}"
        if isinstance(data, list):
            for rank, log in zip(range(len(data)), data):
                self.register_process(f"{log['log_level']}: {log['log_message']}", rank)
        else:
            self.register_process(f"{data['log_level']}: {data['log_message']}")

    def is_valid(self, data: dict) -> bool:
        return all(isinstance(key, str) and
                   isinstance(value, str) for key, value in data.items())


def main():

    def run_task(proc: DataProcessor, cycles: int) -> None:
        for _ in range(cycles):
            proc.output()

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

    print("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")
    run_task(numProcessor, 3)
    run_task(textProcessor, 2)
    run_task(logProcessor, 1)
    d_stream.print_processors_stats()

    # Testing Numeric Processor
    # print("\nTesting Numeric Processor...")
    # print(f"Trying to validate input '42': {numProcessor.validate(42)}")
    # print(f"Trying to validate input 'Hello': "
    #       f"{numProcessor.validate("Hello")}")
    # print("Test invalid ingestion of string 'foo' without prior validation:")
    # try:
    #     numProcessor.ingest("foo")
    # except TypeError as err:
    #     print(err)
    # numProcessor.validate([1, 2, 3, 4, 5])
    # numProcessor.ingest([1, 2, 3, 4, 5])
    # print("Extracting 3 values...")
    # for _ in range(3):
    #     rank, number = numProcessor.output()
    #     print(f"Numeric value {rank}: {number}")

    # # Testing Text Processor
    # print("\nTesting Text Processor...")
    # print(f"Trying to validate input '42': {textProcessor.validate(42)}")
    # textProcessor.validate(['Hello', 'Nexus', 'World'])
    # textProcessor.ingest(['Hello', 'Nexus', 'World'])
    # print("Extracting 3 values...")
    # for _ in range(3):
    #     rank, text = textProcessor.output()
    #     print(f"Text value {rank}: {text}")

    # # Testing Log Processor
    # print("\nTesting Log Processor...")
    # print(f"Trying to validate input 'Hello': "
    #       f"{logProcessor.validate("Hello")}")
    # logProcessor.validate([{'log_level': 'NOTICE',
    #                         'log_message': 'Connection to server'},
    #                        {'log_level': 'ERROR',
    #                         'log_message': 'Unauthorized access!!'}])
    # logProcessor.ingest([{'log_level': 'NOTICE',
    #                       'log_message': 'Connection to server'},
    #                      {'log_level': 'ERROR',
    #                       'log_message': 'Unauthorized access!!'}])
    # print("Extracting 2 values...")
    # for _ in range(2):
    #     rank, log = logProcessor.output()
    #     print(f"Log entry {rank}: {log}")


if __name__ == "__main__":
    main()

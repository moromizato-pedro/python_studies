#!/usr/bin/python3

import abc
import typing


class ExportPlugin(typing.Protocol):
    @abc.abstractmethod
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = ",".join([value for _, value in data])
        print("CSV Ouput:")
        return values


class JSONPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = ",".join([f'"item_{rank}": "{value}"' for rank, value in data])
        print("JSON Ouput:")
        return values


class DataProcessor(abc.ABC):
    def __init__(self):
        super().__init__()
        self.queue = {}
        self.rank = 0
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
        rank, value = list(self.queue.items())[0]
        self.queue.pop(rank)
        self.remaining -= 1
        return (rank, str(value))

    def register_process(self, data: typing.Any) -> None:
        self.queue[self.rank] = data
        self.rank += 1
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            processes = [processor.output() for i in range(nb, 0, -1) 
                         if i <= processor.remaining]
            print(plugin.process_output(processes))


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
                            "expected (<int> | <float> | <list[int | "
                            "float]>)")
        for number in data:
            self.register_process(number)


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
        if isinstance(data, list):
            for text in data:
                self.register_process(text)
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
        if isinstance(data, list):
            for log in data:
                self.register_process(f"{log['log_level']}: "
                                      f"{log['log_message']}")
        else:
            self.register_process(f"{data['log_level']}: "
                                  f"{data['log_message']}")

    def is_valid(self, data: dict) -> bool:
        return all(isinstance(key, str) and
                   isinstance(value, str) for key, value in data.items())


def main():
    def run_task(proc: DataProcessor, cycles: int) -> None:
        for _ in range(cycles):
            proc.output()

    #
    numProcessor = NumericProcessor()
    textProcessor = TextProcessor()
    logProcessor = LogProcessor()
    csvPlugin = CSVPlugin()
    jsonPlugin = JSONPlugin()
    print("=== Code Nexus - Data Stream ===")

    #
    print("\nInitialize Data Stream...")
    d_stream = DataStream()
    d_stream.print_processors_stats()

    #
    print("Registering Processors\n")
    d_stream.register_processor(numProcessor)
    d_stream.register_processor(textProcessor)
    d_stream.register_processor(logProcessor)

    #
    stream = ['Hello world', [3.14, -1, 2.71],
              [{'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'},
               {'log_level': 'INFO',
                'log_message': 'User wil is connected'}],
              42, ['Hi', 'five']]
    
    #
    print(f"Send first batch of data on stream: {stream}\n")
    d_stream.process_stream(stream)
    d_stream.print_processors_stats()

    #
    print("\nSending 3 processed data from each processor to a CSV plugin:")
    d_stream.output_pipeline(3, csvPlugin)
    
    #
    print()
    d_stream.print_processors_stats()

    #
    stream2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'], [{'log_level': 'ERROR', 'log_message': '500 server crash'}, {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {stream2}")
    d_stream.print_processors_stats()

    #
    print("\nSending 5 processed data from each processor to a CSV plugin:")
    d_stream.output_pipeline(5, jsonPlugin)
    


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import sys
import typing


def read_file(file: typing.TextIO) -> None:
    print(f"Accessing file '{file.name}'")
    print("---")
    print()
    content = file.read()
    print(content)
    print()
    print("---")
    file.close()
    print(f"File '{file.name}' closed.")


def main() -> None:
    file = None
    print("=== Cyber Archives Recovery ===")
    try:
        if len(sys.argv) != 2:
            print("Usage: ft_ancient_text.py <file>")
            print()
            return
        file = open(sys.argv[1], 'r')
        read_file(file)
    except (FileNotFoundError, PermissionError) as err:
        print(f"Error opening file '{sys.argv[1]}': {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
    finally:
        if file is not None:
            file.close()
    print()


if __name__ == "__main__":
    main()

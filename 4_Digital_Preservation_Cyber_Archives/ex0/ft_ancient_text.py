#!/usr/bin/env python3

import sys
import typing


def read_file(file_name: str) -> None:
    print(f"Accessing file '{file_name}'")
    file = open(file_name, 'r')
    print("---")
    print()
    content = file.read()
    print(content)
    print("---")
    file.close()
    print(f"File '{file.name}' closed.")


def main():
    print("=== Cyber Archives Recovery ===")
    try:
        if len(sys.argv) != 2:
            print("Usage: ft_ancient_text.py <file>")
            print()
            return
        read_file(sys.argv[1])
    except (FileNotFoundError, PermissionError, IsADirectoryError,
            IOError, OSError, UnicodeEncodeError, MemoryError) as err:
        print(f"Error opening file '{sys.argv[1]}': {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
    print()


if __name__ == "__main__":
    main()

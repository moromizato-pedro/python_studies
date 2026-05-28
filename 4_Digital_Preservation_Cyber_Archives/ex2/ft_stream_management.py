#!/usr/bin/env python3

import sys
import typing


def read_file(file_name: str) -> None:
    file = None
    try:
        file = open(file_name, 'r')
        content = file.read()
        print(content)
    finally:
        if file is not None:
            file.close()


def transform_data(file_name: str) -> list[str]:
    file = None
    try:
        file = open(file_name, 'r')
        lines = file.readlines()
        lines = [line.replace('\n', "#\n") for line in lines]
        lines[-1] += '#'
        return lines
    finally:
        if file is not None:
            file.close()


def save_content(content: list[str], file_name: str) -> bool:
    if not file_name:
        print("Not saving data.")
        return
    print(f"Saving data to {file_name}")
    file = None
    try:
        file = open(file_name, 'w')
        file.writelines(content)
        print(f"Data saved in file {file_name}.")
    except OSError as err:
        print(f"[STDERR] Error opening file '{file_name}': {err}", file=sys.stderr)
        print("Data was not saved.")
    finally:
        if file is not None:
            file.close()


def main():
    print("=== Cyber Archives Recovery ===")
    try:
        if len(sys.argv) != 2:
            print("Usage: ft_ancient_text.py <file>")
            print()
            return

        #
        print(f"Accessing file '{sys.argv[1]}'")
        print("---")
        print()
        read_file(sys.argv[1])
        print()
        print("---")
        print(f"File '{sys.argv[1]}' closed.")
        print()

        #
        print("Transform data:")
        print("---")
        print()
        content = transform_data(sys.argv[1])
        [print(line, end='') for line in content]
        print()
        print("\n---")
        print()

        #
        file_name = input("Enter new file name (or empty):")
        try:
            save_content(content, file_name)
        except OSError as err:
            print(f"[STDERR] Error opening file '{sys.argv[1]}': {err}", file=sys.stderr)
            print("Data not saved.")
    except OSError as err:
        print(f"[STDERR] Error opening file '{sys.argv[1]}': {err}", file=sys.stderr)
    except Exception as err:
        print(f"[STDERR] An unexpected error occurred: {err}", file=sys.stderr)
    print()


if __name__ == "__main__":
    main()

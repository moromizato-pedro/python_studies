#!/usr/bin/env python3

import sys
import typing


def read_file(file_name: str) -> None:
    file = open(file_name, 'r')
    print("---")
    print()
    content = file.read()
    print(content)
    print("---")
    file.close()


def transform_data(file_name: str) -> list[str]:
    file = open(file_name, 'r')
    lines = file.readlines()
    lines = [line.replace('\n', "#\n") for line in lines]
    file.close()
    print("---")
    print()
    [print(line, end='') for line in lines]
    print("\n---")
    return lines


def save_content(content: list[str], file_name: str) -> None:
    if not file_name:
        print("Not saving data.")
        return
    print(f"Saving data to '{file_name}'")
    file = open(file_name, 'w')
    file.writelines(content)
    file.close()
    print(f"Data saved in file '{file_name}'.")


def main():
    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        if len(sys.argv) != 2:
            print("Usage: ft_archive_creation.py <file>")
            print()
            return

        #
        print(f"Accessing file '{sys.argv[1]}'")
        read_file(sys.argv[1])
        print(f"File '{sys.argv[1]}' closed.")
        print()

        #
        print("Transform data:")
        content = transform_data(sys.argv[1])
        print()

        #
        file_name = input("Enter new file name (or empty):")
        save_content(content, file_name)

    except (FileNotFoundError, PermissionError, IsADirectoryError,
            IOError, OSError, UnicodeEncodeError, MemoryError) as err:
        print(f"Error opening file '{sys.argv[1]}': {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
    print()


if __name__ == "__main__":
    main()

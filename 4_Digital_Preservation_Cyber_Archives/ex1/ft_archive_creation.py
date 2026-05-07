#!/usr/bin/env python3

import sys
import typing


def read_file(file_name: str) -> None:
    file = open(file_name, 'r')
    print("---")
    print()
    content = file.read()
    print(content)
    print()
    print("---")
    file.close()


def transform_data(file_name: str):
    file = open(file_name, 'r')
    lines = file.readlines()
    lines = [line.replace('\n', "#\n") for line in lines]
    lines[-1] += '#'
    file.close()
    file = open(file_name, 'w+')
    file.writelines(lines)
    file.close()
    read_file(file_name)


def rename_file(old_name: str, new_name: str) -> None:
    if not new_name:
        print("Not saving data.")
        return
    print(f"Saving data to {new_name}")
    file = open(old_name, 'r')
    content = file.read()
    file.close()
    file = open(new_name, 'w')
    file.write(content)
    file.close()
    print(f"Data saved in file {new_name}.")



def main():
    print("=== Cyber Archives Recovery ===")
    try:
        if len(sys.argv) != 2:
            print("Usage: ft_ancient_text.py <file>")
            print()
            return
        
        #
        print(f"Accessing file '{sys.argv[1]}'")
        read_file(sys.argv[1])
        print(f"File '{sys.argv[1]}' closed.")
        print()

        #
        print("Transform data:")
        transform_data(sys.argv[1])
        print()

        #
        new_name = input("Enter new file name (or empty):")
        rename_file(sys.argv[1], new_name)

    except (FileNotFoundError, PermissionError, IsADirectoryError,
            IOError, OSError, UnicodeEncodeError, MemoryError) as err:
        print(f"Error opening file '{sys.argv[1]}': {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
    print()


if __name__ == "__main__":
    main()

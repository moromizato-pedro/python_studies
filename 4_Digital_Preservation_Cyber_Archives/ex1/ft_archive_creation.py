#!/usr/bin/env python3

import sys


def read_file(file_name: str) -> str:
    f = None
    content = ""
    try:
        f = open(file_name)
        content = f.read()
        print("---")
        print()
        print(content)
        print()
        print("---")
    finally:
        if f is not None:
            f.close()
    return content


def transform_data(content: str) -> str:
    lines = [line + '#' for line in content.split('\n')]
    return '\n'.join(lines)


def save_file(new_name: str, content: str) -> None:
    f = None
    try:
        f = open(new_name, 'w')
        f.write(content)
    finally:
        if f is not None:
            f.close()


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        print()
        return

    print(f"Accessing file '{sys.argv[1]}'")
    try:
        content = read_file(sys.argv[1])
    except (FileNotFoundError, PermissionError) as err:
        print(f"Error opening file "
              f"'{sys.argv[1]}': {err}", file=sys.stderr)
        return
    print(f"File '{sys.argv[1]}' closed.")
    print()

    print("Transform data:")
    print("---")
    print()
    content = transform_data(content)
    print(content)
    print()
    print("---")
    print()

    new_name = None
    try:
        new_name = input("Enter new file name (or empty):")
    except (EOFError, KeyboardInterrupt):
        print("\nInput canceled.")
    if not new_name:
        print("Not saving data.")
        return
    print(f"Saving data to {new_name}")
    try:
        save_file(new_name, content)
        print(f"Data saved in file {new_name}.")
    except (FileNotFoundError, PermissionError) as err:
        print(f"Error opening file '{new_name}': {err}", file=sys.stderr)
        print("Data not saved.")
    print()


if __name__ == "__main__":
    main()

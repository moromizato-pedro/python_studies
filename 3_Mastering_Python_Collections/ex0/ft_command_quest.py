#!/usr/bin/python3

import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv[1:]) > 0:
        print(f"Arguments received: {len(sys.argv[1:])}")
        for arg in sys.argv[1:]:
            print(f"Argument {sys.argv.index(arg)}: {arg}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(sys.argv)}\n")


if __name__ == "__main__":
    main()

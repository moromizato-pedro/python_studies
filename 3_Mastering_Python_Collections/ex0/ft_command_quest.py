#!/usr/bin/python3

import sys


#   Using range()
#   arg_count = len(sys.argv)
#   if arg_count - 1 > 0
#       print(f"Arguments received: {arg_count - 1}")
#       for i in range(1, arg_count):
#           print(f"Argument {i}: {sys.argv[i]}")
#   Using negative index
#       for arg in sys.argv[-arg_count:]:
#           print(f"Argument {i}: {sys.argv[i]}")
def main():
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

#!/usr/bin/env python3

import sys
import os


def warn_global_environment() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {os.path.realpath(sys.executable)}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print()
    print("Then run this program again.")


def show_construct() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {sys.prefix.split('/')[-1]}")
    print(f"Environment Path: {sys.prefix}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    for path in sys.path:
        if "site-packages" in path:
            print(path)


if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        warn_global_environment()
    else:
        show_construct()

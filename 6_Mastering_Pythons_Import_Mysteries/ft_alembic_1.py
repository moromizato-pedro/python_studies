#!/usr/bin/env python3


from elements import create_water


def main():
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}")
    print()


if __name__ == "__main__":
    main()

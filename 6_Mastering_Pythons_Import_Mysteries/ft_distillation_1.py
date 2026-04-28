#!/usr/bin/env python3


import alchemy


def main():
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.special_heal()}")
    print()


if __name__ == "__main__":
    main()

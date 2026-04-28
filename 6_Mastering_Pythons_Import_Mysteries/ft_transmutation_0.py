#!/usr/bin/env python3


import alchemy.transmutation.recipes as recipes


def main():
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(f"Testing lead to gold: {recipes.lead_to_gold()}")
    print()


if __name__ == "__main__":
    main()

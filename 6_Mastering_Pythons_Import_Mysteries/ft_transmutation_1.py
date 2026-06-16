#!/usr/bin/env python3

import alchemy.transmutation as transmut


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {transmut.lead_to_gold()}")
    print()


if __name__ == "__main__":
    main()

#!/usr/bin/python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
               'kevin', 'Liam']
    print(f"\nInitial list of players: {players}")

    #
    capitalize_all = [name.capitalize() for name in players]
    print(f"\nNew list with all names capitalized: {capitalize_all}")

    #
    only_capitalized = [name for name in players if name.istitle()]
    print(f"\nNew list of capitalized names only: {only_capitalized}")

    #
    scored_dict = {name: random.randint(0, 1000) for name in capitalize_all}
    print(f"\nScore dict: {scored_dict}")

    #
    avg_score = sum(scored_dict.values())/len(scored_dict)
    print(f"\nScore average is {avg_score:.2f}")

    #
    high_scores = {name: score for name, score in scored_dict.items()
                   if score > avg_score}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()

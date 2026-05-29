#!/usr/bin/python3

import random


def gen_player_achievements(all: bool = False) -> set[str]:
    achievements_list = [
        "[1] Boss Slayer",
        "[2] Collector Supreme",
        "[3] Crafting Genius",
        "[4] First Steps",
        "[5] Hidden Path Finder",
        "[6] Master Explorer",
        "[7] Sharp Mind",
        "[8] Speed Runner",
        "[9] Strategist",
        "[10] Survivor",
        "[11] Treasure Hunter",
        "[12] Unstoppable",
        "[13] Untouchable",
        "[14] World Savior"
    ]
    if all:
        return set(achievements_list)
    half = int(len(achievements_list) / 2)
    quantity = random.randint(3, half + 2)
    return set(random.sample(achievements_list, quantity))


class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self._achievements: set[str] = set()

    def gen_achievements(self) -> None:
        self._achievements = gen_player_achievements()

    def get_achievements(self) -> set[str]:
        return self._achievements


def main() -> None:
    #   Setup
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    players: list[Player] = []
    for name in names:
        players.append(Player(name))
    for player in players:
        player.gen_achievements()
    print("=== Achievements Tracker System ===\n")

    # Players sets
    distinct: set[str] = set()
    common = players[0].get_achievements()
    for player in players:
        print(f"Player {player.name}: {player.get_achievements()}")
        distinct = distinct.union(player.get_achievements())
        common = common.intersection(player.get_achievements())

    # Distinct achievements
    print(f"\nAll distinct achievements: {distinct}")

    # Common achievements
    print(f"\nCommon achievements: {common}\n")

    # Unique achievements per player
    others = players.copy()
    others_achiv: set[str] = set()
    diff: set[str] = set()
    for player in players:
        others_achiv.clear()
        diff.clear()
        others.remove(player)
        for other in others:
            others_achiv = others_achiv.union(other.get_achievements())
        diff = player.get_achievements().difference(others_achiv)
        print(f"Only {player.name} has: {diff}")
        others.append(player)
    all = gen_player_achievements(True)

    # Missing achievements
    print()
    for player in players:
        print(f"{player.name} is missing: "
              f"{all.difference(player.get_achievements())}")


if __name__ == "__main__":
    main()

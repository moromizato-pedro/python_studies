#!/usr/bin/python3

import random


class Achievements():
    def __init__(self):
        pass

    @staticmethod
    def get_all() -> list:
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
        return achievements_list


class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.__achievements: set[str] = set()
        self.gen_player_achievements()

    def gen_player_achievements(self) -> None:
        quantity = random.randrange(len(Achievements().get_all()))
        self.__achievements = set()
        while len(self.__achievements) < quantity:
            self.__achievements.add(random.choice(Achievements().get_all()))

    def get_achievements(self) -> set:
        return self.__achievements

    def add_achievement(self, achievement: str) -> None:
        if achievement in Achievements().get_all():
            self.__achievements.add(achievement)

    def remove_achievement(self, achievement: str) -> None:
        if achievement in self.__achievements:
            self.__achievements.remove(achievement)


def main():
    #   Setup
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    players = []
    for name in names:
        players.append(Player(name))
    print("=== Achievements Tracker System ===")

    # Players sets
    distinct = set()
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
    others_achiv = set()
    diff = set()
    unique = []
    for player in players:
        others_achiv.clear()
        diff.clear()
        others.remove(player)
        for other in others:
            others_achiv = others_achiv.union(other.get_achievements())
        diff = player.get_achievements().difference(others_achiv)
        unique.append(diff)
        print(f"Only {player.name} has: {diff}")
        others.append(player)

    # Missing achievements
    print()
    missing = []
    for player in players:
        missing.append(distinct.difference(player.get_achievements()))
        print(f"{player.name} is missing: "
              f"{distinct.difference(player.get_achievements())}")


if __name__ == "__main__":
    main()

    # Checkers:
    # Insert the line below at the end of main()
    # checker(players, distinct, common, unique, missing)

    # Substitute gen_player_achievements by this one with the example values
    # def gen_player_achievements(self) -> set:
    #     ach = set()
    #     if self.name == "Alice":
    #         ach = ach.union({'Crafting Genius', 'World Savior',
    #                          'Master Explorer', 'Collector Supreme',
    #                          'Untouchable', 'Boss Slayer'})
    #     elif self.name == "Bob":
    #         ach = ach.union({'Crafting Genius', 'Strategist', 'World Savior',
    #                          'Master Explorer', 'Unstoppable',
    #                          'Collector Supreme', 'Untouchable'})
    #     elif self.name == "Charlie":
    #         ach = ach.union({'Strategist', 'Speed Runner', 'Survivor',
    #                          'Master Explorer', 'Treasure Hunter',
    #                          'First Steps', 'Collector Supreme',
    #                          'Untouchable', 'Sharp Mind'})
    #     elif self.name == "Dylan":
    #         ach = ach.union({'Strategist', 'Speed Runner', 'Unstoppable',
    #                          'Untouchable', 'Boss Slayer'})
    #     self.__achievements = ach


# def checker(players: list, distinct: set, common: set, unique: list,
#             missing: list) -> None:
#     print("\n=== Checkers ===")
#     check_expected_player_sets(players)
#     check_distinct(distinct)
#     check_common(common)
#     check_only(players, unique)
#     check_missing(players, missing)


# def check_expected_player_sets(players: list) -> None:
#     checker = []
#     print("\n=== Player original set")
#     checker.append({'Crafting Genius', 'World Savior', 'Master Explorer',
#                     'Collector Supreme', 'Untouchable', 'Boss Slayer'})
#     checker.append({'Crafting Genius', 'Strategist', 'World Savior',
#                     'Master Explorer', 'Unstoppable', 'Collector Supreme',
#                     'Untouchable'})
#     checker.append({'Strategist', 'Speed Runner', 'Survivor',
#                     'Master Explorer', 'Treasure Hunter', 'First Steps',
#                     'Collector Supreme', 'Untouchable', 'Sharp Mind'})
#     checker.append({'Strategist', 'Speed Runner', 'Unstoppable',
#                     'Untouchable', 'Boss Slayer'})
#     for player, check in zip(players, checker):
#         diff = player.get_achievements().difference(check)
#         if diff:
#             raise ValueError(f"{player.name} set [KO] | diff: {diff}")
#         print(f"{player.name} set [OK]")


# def check_distinct(distinct: set) -> None:
#     print("\n=== Players distinct achievements")
#     checker = {'Crafting Genius', 'Strategist', 'World Savior',
#                'Speed Runner', 'Survivor', 'Master Explorer',
#                'Treasure Hunter', 'Unstoppable', 'First Steps',
#                'Collector Supreme', 'Untouchable', 'Sharp Mind',
#                'Boss Slayer'}
#     if distinct.difference(checker):
#         raise ValueError("Distinct set [KO] | "
#                          f"diff: {distinct.difference(checker)}")
#     print("Distinct set [OK]")


# def check_common(common: set) -> None:
#     print("\n=== Players common achievements")
#     checker = {'Untouchable'}
#     if common.difference(checker):
#         raise ValueError("Common set [KO] | "
#                          f"diff: {common.difference(checker)}")
#     print("Common set [OK]")


# def check_only(players: list, uniques: list) -> None:
#     checker = []
#     print("\n=== Player unique achievements")
#     checker.append(set())
#     checker.append(set())
#     checker.append({'Survivor', 'Treasure Hunter', 'First Steps',
#                     'Sharp Mind'})
#     checker.append(set())
#     for player, unique, check in zip(players, uniques, checker):
#         if unique.difference(check):
#             raise ValueError(f"Only {player.name} set [KO] | "
#                              f"diff: {unique.difference(check)}")
#         print(f"Only {player.name} set [OK]")


# def check_missing(players: list, missing: list) -> None:
#     checker = []
#     print("\n=== Player missing achievements")
#     checker.append({'Strategist', 'Speed Runner', 'Survivor',
#                     'Treasure Hunter', 'Unstoppable', 'Hidden Path Finder',
#                     'First Steps', 'Sharp Mind'})
#     checker.append({'Speed Runner', 'Survivor', 'Treasure Hunter',
#                     'Hidden Path Finder', 'First Steps', 'Sharp Mind',
#                     'Boss Slayer'})
#     checker.append({'Crafting Genius', 'World Savior', 'Hidden Path Finder',
#                     'Unstoppable', 'Boss Slayer'})
#     checker.append({'Crafting Genius', 'World Savior',
#                     'Survivor', 'Master Explorer', 'Treasure Hunter',
#                     'Hidden Path Finder', 'First Steps', 'Collector Supreme',
#                     'Sharp Mind'})
#     for player, miss, check in zip(players, missing, checker):
#         if miss.difference(check):
#             raise ValueError(f"Only {player.name} set [KO] | "
#                              f"diff: {miss.difference(check)}")
#         print(f"Only {player.name} set [OK]")

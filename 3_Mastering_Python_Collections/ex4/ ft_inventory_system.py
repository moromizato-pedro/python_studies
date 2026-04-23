#!/usr/bin/python3

import sys


class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.inventory = self.__starter_items()

    def __starter_items(self) -> dict:
        inventory = {}
        for arg in sys.argv[1:]:
            try:
                if len(arg.split(':')) < 2:
                    raise SyntaxError(f"Error - invalid parameter '{arg}'")
                item, quantity = arg.split(':')
                if item not in inventory:
                    inventory[item] = int(quantity)
                else:
                    raise ValueError(f"Reduntant item '{item}' - discarding")
            except SyntaxError as err:
                print(err)
            except TypeError as err:
                print(f"Quantity error for '{item}': {err}")
            except ValueError as err:
                print(f"Quantity error for '{item}': {err}")
        return inventory

    def add_item(self, item: str, quantity: int) -> None:
        if item not in self.inventory:
            self.inventory[item] = quantity

    def remove_item(self, item: str) -> None:
        if item in self.inventory:
            self.inventory.pop(item)


def main():
    print("=== Inventory System Analysis ===")
    player = Player("Ana")
    print(f"Got inventory: {player.inventory}")
    print(f"Item list: {list(player.inventory.keys())}")
    print(f"Total quantity of the {len(player.inventory)} "
          "items: {sum(player.inventory.values())}")
    most_abundant = None
    least_abundant = None
    for item in player.inventory.items():
        print(f"Item {item[0]} represents "
              f"{item[1] / sum(player.inventory.values()) * 100:.1f}%")
        if not most_abundant or most_abundant[1] < item[1]:
            most_abundant = item
        if not least_abundant or least_abundant[1] > item[1]:
            least_abundant = item
    print(f"Item most abundant: {most_abundant[0]} with "
          f"quantity {most_abundant[1]}")
    print(f"Item least abundant: {least_abundant[0]} with "
          f"quantity {least_abundant[1]}")
    player.add_item("magic_item", 1)
    print(f"Updated inventory: {player.inventory}")


if __name__ == "__main__":
    main()

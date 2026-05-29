#!/usr/bin/python3

import sys


class InventoryError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self._inventory: dict[str, int] = {}

    def fill_inventory(self) -> None:
        item = None
        quantity = None
        for arg in sys.argv[1:]:
            try:
                self.validate_argument(arg)
                item, quantity = arg.split(':')
                self.add_item(item, quantity)
            except (SyntaxError, InventoryError) as err:
                print(err)
            except ValueError as err:
                print(f"Quantity error for '{item}': {err}")

    def validate_argument(self, arg: str) -> None:
        if len(arg.split(':')) != 2:
            raise SyntaxError(f"Error - invalid parameter '{arg}'")

    def add_item(self, item: str, quantity: str) -> None:
        if item not in self.get_inventory():
            self.get_inventory()[item] = int(quantity)
        else:
            raise InventoryError(f"Reduntant item '{item}' - discarding")

    def get_inventory(self) -> dict[str, int]:
        return self._inventory

    def remove_item(self, item: str) -> None:
        if item in self.get_inventory():
            self.get_inventory().pop(item)


def main() -> None:
    print("=== Inventory System Analysis ===")
    player = Player("Ana")
    player.fill_inventory()
    print(f"Got inventory: {player.get_inventory()}")
    print(f"Item list: {list(player.get_inventory().keys())}")
    print(f"Total quantity of the {len(player.get_inventory())} "
          f"items: {sum(player.get_inventory().values())}")
    most_name = least_name = ""
    most_quant = least_quant = 0
    for item in player.get_inventory().items():
        name, quantity = item
        percentage = quantity / sum(player.get_inventory().values()) * 100
        print(f"Item {name} represents "
              f"{round(percentage, 1)}%")
        if not most_name or most_quant < quantity:
            most_name, most_quant = item
        if not least_name or least_quant > quantity:
            least_name, least_quant = item
    print(f"Item most abundant: {most_name} with "
          f"quantity {most_quant}")
    print(f"Item least abundant: {least_name} with "
          f"quantity {least_quant}")
    player.add_item("magic_item", "1")
    print(f"Updated inventory: {player.get_inventory()}")


if __name__ == "__main__":
    main()

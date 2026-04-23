#!/usr/bin/python3

class Plant:
    def __init__(self, name, height, age, period=1, growth=0.8):
        self.name = name
        self._height = height
        self._age = age
        self.period = period
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += self.growth

    def age(self) -> None:
        self._age += self.period

#   Getters
    def get_age(self) -> int:
        return self._age

    def get_height(self) -> int:
        return self._height

#   Setters
    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self.name}: Error: age can't be negative")
            print("Age update rejected")

    def set_height(self, height: int) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self.name}: Error: height can't be negative")
            print("Height update rejected")


def main():
    plant = Plant("Rose", 15, 10)

#   ===========================
    print("=== Garden Security System ===")
    print("Plant created: ", end='')
    plant.show()
    print()

#   ===========================
    plant.set_height(25)
    plant.set_age(30)
    print()

#   ===========================
    plant.set_height(-1)
    plant.set_age(-5)
    print()

#   ===========================
    print("Current state: ", end='')
    plant.show()


if __name__ == "__main__":
    main()

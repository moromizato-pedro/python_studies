#!/usr/bin/python3

class Plant:
    def __init__(self, name, height, age, period: int = 1,
                 growth: float = 0.8):
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


class Flower(Plant):
    def __init__(self, name, height, age, color: str,
                 period=1, growth=0.8, bloom: bool = False) -> None:
        super().__init__(name, height, age, period, growth)
        self.color = color
        self.has_bloomed = bloom

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.has_bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        if not self.has_bloomed:
            print(f"[asking the {self.name} to bloom]")
            self.has_bloomed = True


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: float,
                 period=1, growth=0.8) -> None:
        super().__init__(name, height, age, period, growth)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.get_height()}cm"
              f" long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season: str,
                 nutritional_value: int, period=1, growth=2.1) -> None:
        super().__init__(name, height, age, period, growth)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def increase_nutritional_value(self, days: int) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        for day in range(days):
            super().age()
            super().grow()
            self.nutritional_value += 1


def main():
    flower = Flower("Rose", 15.0, 10, "red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    print("=== Garden Plant Types ===")

#   ===========================
    print("=== Flower")
    flower.show()
    flower.bloom()
    flower.show()
    print()

#   ===========================
    print("=== Tree")
    tree.show()
    tree.produce_shade()
    print()

#   ===========================
    print("=== Vegetable")
    vegetable.show()
    vegetable.increase_nutritional_value(20)
    vegetable.show()


if __name__ == "__main__":
    main()

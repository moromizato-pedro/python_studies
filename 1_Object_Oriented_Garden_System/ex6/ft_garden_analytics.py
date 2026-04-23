#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int, period: int = 1,
                 growth: float = 0.8):
        self.name = name
        self._height = height
        self._age = age
        self.period = period
        self.growth = growth
        self.stats = self.Stats(0, 0, 0, 0)

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")
        self.stats.set_showed(self.stats.get_showed() + 1)

    def grow(self) -> None:
        self._height += self.growth
        self.stats.set_growed(self.stats.get_growed() + 1)

    def age(self) -> None:
        self._age += self.period
        self.stats.set_aged(self.stats.get_aged() + 1)

#   Getters
    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
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

    @staticmethod
    def is_older_1_year(days: int):
        print(f"Is {days} days more than a year? -> ", end='')
        if days > 365:
            print("True")
        else:
            print("False")

    @classmethod
    def Anonymous(cls):
        return cls("Unknown plant", 0.0, 0, 0, 0.0)

#   Subclasses
    class Stats:
        def __init__(self, growed: int, aged: int, showed: int,
                     shades_produced: int) -> None:
            self._growed = growed
            self._aged = aged
            self._showed = showed
            self._shades_produced = shades_produced

        def set_growed(self, growed: int) -> None:
            self._growed = growed

        def set_aged(self, aged: int) -> None:
            self._aged = aged

        def set_showed(self, showed: int) -> None:
            self._showed = showed

        def set_shades_produced(self, shades_produced: int) -> None:
            self._shades_produced = shades_produced

        def get_growed(self) -> int:
            return self._growed

        def get_aged(self) -> int:
            return self._aged

        def get_showed(self) -> int:
            return self._showed

        def get_shades_produced(self) -> int:
            return self._shades_produced


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str,
                 period: int = 1, growth: float = 0.8,
                 bloom: bool = False) -> None:
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
            self.has_bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, period: int = 1,
                 growth: float = 0.8) -> None:
        super().__init__(name, height, age, period, growth)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.get_height()}cm"
              f" long and {self.trunk_diameter}cm wide.")
        self.stats.set_shades_produced(self.stats.get_shades_produced() + 1)


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str,
                 period: int = 1, growth: float = 0.8, bloom=False,
                 seed_quantity: int = 0, seeds: int = 0) -> None:
        super().__init__(name, height, age, color, period, growth, bloom)
        self.seeds = seeds
        self.seed_quantity = seed_quantity

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds += self.seed_quantity


def show_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    print(f"Stats: {plant.stats.get_growed()} grow, {plant.stats.get_aged()}"
          f" age, {plant.stats.get_showed()} show")
    if type(plant).__name__ == "Tree":
        print(f" {plant.stats.get_shades_produced()} shade")


def main():
    garden = []
    garden.append(Flower("Rose", 15.0, 10, "red", growth=8.0))
    garden.append(Tree("Oak", 200.0, 365, 5.0))
    garden.append(Seed("Sunflower", 80.0, 45, "yellow", 20, 30.0,
                       seed_quantity=42))
    garden.append(Plant.Anonymous())
    print("=== Garden statistics ===")

#   ===========================
    print("== Check year-old")
    Plant.is_older_1_year(30)
    Plant.is_older_1_year(400)

    for plant in garden:
        plant_type = type(plant).__name__

        # Title
        if (plant_type == "Plant"):
            print("\n=== Anonymous")
        else:
            print(f"\n=== {plant_type}")

        # Initial Information
        plant.show()

        # Initial Statistics
        if (plant_type not in ["Plant", "Seed"]):
            show_statistics(plant)

        # Applying Modifications
        if (plant_type == "Flower"):
            print("[asking the rose to grow and bloom]")
            plant.bloom()
            plant.grow()
            plant.show()
        elif (plant_type == "Tree"):
            print("[asking the oak to produce shade]")
            plant.produce_shade()
        elif (plant_type == "Seed"):
            print("[make sunflower grow, age and bloom]")
            plant.grow()
            plant.age()
            plant.bloom()
            plant.show()

        # Final Statistics
        show_statistics(plant)


if __name__ == "__main__":
    main()

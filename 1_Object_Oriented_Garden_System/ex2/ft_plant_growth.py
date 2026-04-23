#!/usr/bin/python3

class Plant:
    def __init__(self, name, height, age, period=1, growth=0.8):
        self.name = name
        self.height = height
        self.age_days = age
        self.period = period
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.age_days += self.period


def main():
    plants = []
    plants.append(Plant("Rose", 25.0, 30))
    initial_height = plants[0].height
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plants[0].show()
        plants[0].grow()
        plants[0].age()
    print(f"Growth this week: {plants[0].height - initial_height:.1f}cm")


if __name__ == "__main__":
    main()

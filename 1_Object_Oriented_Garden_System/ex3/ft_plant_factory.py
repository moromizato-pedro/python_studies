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
    plants.append(Plant("Oak", 200.0, 365))
    plants.append(Plant("Cactus", 5.0, 90))
    plants.append(Plant("Sunflower", 80.0, 45))
    plants.append(Plant("Fern", 15.0, 120))
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end='')
        plant.show()


if __name__ == "__main__":
    main()

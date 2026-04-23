#!/usr/bin/python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    plants = [Plant("Rose", 25, 30),
              Plant("Sunflower", 80, 45),
              Plant("Cactus", 15, 120)]
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()

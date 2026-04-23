#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Caught GardenError: {self.message}"


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Caught PlantError: {self.message}"


def water_plant(plant_name: str) -> None:
    if plant_name == str.capitalize(plant_name):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as err:
        print(err)
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main():
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print("\nTesting invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()

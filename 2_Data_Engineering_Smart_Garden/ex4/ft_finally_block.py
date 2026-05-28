#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


def water_plant(plant_name: str) -> None:
    if plant_name == str.capitalize(plant_name):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plant1: str, plant2: str, plant3: str) -> None:
    print("Opening watering system")
    try:
        water_plant(plant1)
        water_plant(plant2)
        water_plant(plant3)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print("... ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    test_watering_system("Tomato", "Lettuce", "Carrots")

    print("\nTesting invalid plants...")
    test_watering_system("Tomato", "lettuce", "Carrots")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()

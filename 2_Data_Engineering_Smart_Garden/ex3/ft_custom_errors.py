#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        self.message = message
        super().__init__(self.message)


def input_temperature(name: str, temp_str: str) -> float:
    print(f"Input data is '{temp_str}'")
    temp = float(temp_str)
    if temp > 40.0:
        raise PlantError(f"The {name} is wilting!")
    if temp < 0.0:
        raise PlantError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def input_water(water_level: str) -> int:
    print(f"Input data is '{water_level}'")
    tank_level = int(water_level)
    if tank_level > 50:
        raise WaterError("Too much water in the tank!")
    if tank_level < 5:
        raise WaterError("Not enough water in the tank!")
    return tank_level


def test_plant_errors(name: str, temp: str) -> None:
    try:
        print(f"Temperature is now {input_temperature(name, temp)}°C")
    except PlantError as err:
        print(f"Caught PlantError: {err}")


def test_water_errors(water_in_cl: str) -> None:
    try:
        print(f"Water level is now {input_water(water_in_cl)}cl")
    except WaterError as err:
        print(f"Caught WaterError: {err}")


def test_garden_errors() -> None:
    try:
        input_temperature("tomato", "41.2")
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    try:
        input_water("1")
    except GardenError as err:
        print(f"Caught GardenError: {err}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    test_plant_errors("tomato", "40.1")
    test_plant_errors("tomato", "-5.2")
    test_plant_errors("tomato", "0")

    print("\nTesting WaterError...")
    test_water_errors("0")
    test_water_errors("51")
    test_water_errors("6")

    print("\nTesting catching all garden errors...")
    test_garden_errors()

    print("\nAll custom error types work correctly")


if __name__ == "__main__":
    main()

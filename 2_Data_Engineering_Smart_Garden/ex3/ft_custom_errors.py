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


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Caught WaterError: {self.message}"


def test_plant_errors(plant_temperature: float, hours_exposed: int) -> None:
    if plant_temperature > 40.0:
        if hours_exposed > 3 and hours_exposed < 5:
            raise PlantError("The plant is wilting")
        elif hours_exposed > 5:
            raise PlantError("The plant is wilted")
    else:
        print("No PlantErrors!")


def test_water_errors(tank_level: int) -> None:
    if tank_level < 10:
        raise WaterError("Not enough water in the tank")
    elif tank_level > 500:
        raise WaterError("Too much water in the tank")
    else:
        print("No WaterErrors!")


def test_garden_errors(func, params: list):
    try:
        func(*params)
    except GardenError as err:
        print(f"{GardenError.__str__(err)}")


def main():
    print("=== Custom Garden Errors Demo ===")

    #
    print("\n----- Testing PlantError...")
    plant_tests = [
        (42.0, 4),
        (42.0, 6)
    ]
    for temp, period in plant_tests:
        try:
            test_plant_errors(temp, period)
        except PlantError as err:
            print(err)

    #
    print("\n----- Testing WaterError...")
    water_tests = [
        0,
        600
    ]
    for level in water_tests:
        try:
            test_water_errors(level)
        except WaterError as err:
            print(err)

    #
    print("\n----- Testing catching all garden errors...")
    test_garden_errors(test_plant_errors, (42.0, 4))
    test_garden_errors(test_water_errors, ((0,)))

    print("\n----- Testing standard Errors...")
    try:
        raise PlantError()
    except PlantError as err:
        print(err)
    try:
        raise WaterError()
    except WaterError as err:
        print(err)
    try:
        raise GardenError()
    except GardenError as err:
        print(err)

    print("\n----- Testing Valid Results...")
    try:
        print("-- PlantErrors:")
        test_plant_errors(30.0, 50)
    except PlantError as err:
        print(err)
    try:
        print("-- WaterErrors:")
        test_water_errors(200)
    except WaterError as err:
        print(err)
    try:
        print("-- GardenErrors:")
        test_garden_errors(test_plant_errors, (30.0, 50))
        test_garden_errors(test_water_errors, ((200,)))
    except GardenError as err:
        print(err)


if __name__ == "__main__":
    main()

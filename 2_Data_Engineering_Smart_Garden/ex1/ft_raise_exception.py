#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature(temp: str) -> None:
    try:
        print(f"Temperature is now {input_temperature(temp)}°C\n")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}\n")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()

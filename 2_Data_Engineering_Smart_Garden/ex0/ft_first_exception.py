#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    print(f"Temperature is now {int(temp_str)}°C\n")
    return int(temp_str)


def test_temperature(temp: str) -> None:
    try:
        input_temperature(temp)
    except ValueError as err:
        print(f"Caught input_temperature error: {err}\n")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature("25")
    test_temperature("abc")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()

#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    try:
        print(f"Input data is '{temp_str}'")
        res = int(temp_str)
        print(f"Temperature is now {res}°C\n")
        return res
    except Exception as err:
        print(f"Caught input_temperature error: {err}")
        return 0


def test_temperature() -> None:
    input_temperature("25")
    input_temperature("abc")


def main():
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()

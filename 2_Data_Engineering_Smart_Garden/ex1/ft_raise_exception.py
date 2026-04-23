#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    try:
        print(f"Input data is '{temp_str}'")
        res = int(temp_str)
        if res < 0:
            raise Exception(f"{res}°C is too cold for plants (min 0°C)")
        if res > 40:
            raise Exception(f"{res}°C is too hot for plants (max 40°C)")
        print(f"Temperature is now {res}°C\n")
        return res
    except Exception as err:
        print(f"Caught input_temperature error: {err}\n")
        return 0


def test_temperature() -> None:
    input_temperature("25")
    input_temperature("abc")
    input_temperature("100")
    input_temperature("-50")


def main():
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()

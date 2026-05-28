#!/usr/bin/python3

def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        int(5 / 0)
    elif operation_number == 2:
        open('/non/existent/file')
    elif operation_number == 3:
        str("Hello" + 5)
    else:
        print("Operation completed successfully")
        return


def test_error_types(operation: int) -> None:
    try:
        garden_operations(operation)
    except ValueError as err:
        print(f"Caught ValueError: {err}")
    except ZeroDivisionError as err:
        print(f"Caught ZeroDivisionError: {err}")
    except FileNotFoundError as err:
        print(f"Caught FileNotFoundError: {err}")
    except TypeError as err:
        print(f"Caught TypeError: {err}")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types(0)
    test_error_types(1)
    test_error_types(2)
    test_error_types(3)
    test_error_types(4)
    print("\nAll error types tested seccessfully!")


if __name__ == "__main__":
    main()

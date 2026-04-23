#!/usr/bin/python3

def garden_operations(operation_number: int):
    print(f"Testing operation {operation_number}...")
    try:
        if operation_number == 0:
            int("abc")
        elif operation_number == 1:
            return 5/0
        elif operation_number == 2:
            open('/non/existent/file')
        elif operation_number == 3:
            return "Hello" + 5
        else:
            print("Operation completed successfully")
            return
    except Exception as err:
        print(f"Caught {err.__class__.__name__}: {err}")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations(0)
    garden_operations(1)
    garden_operations(2)
    garden_operations(3)
    garden_operations(4)
    print("\nAll tests completed - program didn't crash!")


def main():
    test_error_types()


if __name__ == "__main__":
    main()

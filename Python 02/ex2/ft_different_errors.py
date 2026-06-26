def garden_operations(operation_number: int) -> None:
    match (operation_number):
        case 0:
            int("abc")
            raise
        case 1:
            4/0
            raise
        case 2:
            open("/non/existent/file.txt")
            raise
        case 3:
            "Error" + 2
            raise
        case _:
            return


def test_error_types() -> None:
    test_values = [0, 1, 2, 3, 4]
    print("=== Garden Error Types Demo ===")
    for value in test_values:
        print(f"Testing operation {value}...")
        try:
            garden_operations(value)
            print("Operation completed successfully")
        except ValueError as ex:
            print(f"Caught ValueError: {ex}")
        except ZeroDivisionError as ex:
            print(f"Caught ZeroDivisionError: {ex}")
        except FileNotFoundError as ex:
            print(f"Caught FileNotFoundError: {ex}")
        except TypeError as ex:
            print(f"Caught TypeError: {ex}")


def main() -> None:
    test_error_types()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()

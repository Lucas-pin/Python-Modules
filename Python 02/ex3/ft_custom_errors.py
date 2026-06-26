class GardenError(Exception):
    """Base class for exceptions in the garden module."""
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    """Exception raised for errors related to plants."""
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    """Exception raised for errors related to watering."""
    def __init__(self, message: str = "Unknown watering error"):
        super().__init__(message)


def test_exceptions(exception_type: int) -> None:
    """Function to test custom exceptions."""
    match exception_type:
        case 0:
            raise PlantError("The tomato plant is wilting!")
        case 1:
            raise WaterError("Not enough water in the tank!")


def main() -> None:
    """Main function to run the exception tests."""
    print("=== Custom Garden Errors Demo ===")
    try:
        print("Testing PlantError...")
        test_exceptions(0)
    except PlantError as ex:
        print(f"Caught PlantError: {ex}")
    try:
        print("Testing WaterError...")
        test_exceptions(1)
    except WaterError as ex:
        print(f"Caught WaterError: {ex}")
    for value in (0, 1):
        try:
            print("Testing catching all garden errors...")
            test_exceptions(value)
        except GardenError as ex:
            print(f"Caught GardenError: {ex}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()

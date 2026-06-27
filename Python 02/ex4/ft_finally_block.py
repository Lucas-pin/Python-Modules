class GardenError(Exception):
    """Base class for exceptions in the garden module."""
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    """Exception raised for errors related to plants."""
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if str.capitalize(plant_name) == plant_name:
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    plant_list = ["Letucce", "Tomato", "Bananas"]
    invalid_plant_list = ["tomato", "Letucce", "Bananas"]

    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        for plant in plant_list:
            water_plant(plant)

        print("\nTesting invalid plants...")
        for plant in invalid_plant_list:
            water_plant(plant)
    except PlantError as ex:
        print(f"Caught PlantError: {ex}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===")
    test_watering_system()


if __name__ == "__main__":
    main()

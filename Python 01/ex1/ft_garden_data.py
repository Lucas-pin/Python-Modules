class Plant:
    '''A Plant class that stores information about a plant.
    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        plant_age (int): The age of the plant in days.
    Methods:
        show(): Prints the plant's information in a formatted string.
    '''

    def __init__(self, name: str = "default",
                 height: int = 0,
                 age: int = 0) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    first_plant: Plant = Plant("Rose", 25, 30)
    second_plant: Plant = Plant("Sunflower", 80, 45)
    third_plant: Plant = Plant("Cactus", 15, 120)
    first_plant.show()
    second_plant.show()
    third_plant.show()


if __name__ == "__main__":
    main()

class Plant:
    '''A Plant class that stores information about a plant.
    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        plant_age (int): The age of the plant in days.
    Methods:
        show(): Prints the plant's information in a formatted string.
        grow(): Increases the height of the plant by a specified amount.
        age(): Increases the age of the plant by a specified number of days.
    '''

    def __init__(self, name: str = "default",
                 height: float = 0.0,
                 age: int = 0) -> None:
        self.name = name
        self.height = height
        self.initial_height = height
        self.plant_age = age

    def grow(self, height: float) -> None:
        self.height += height
        self.total_height = self.height - self.initial_height

    def age(self, age: int = 1) -> None:
        self.plant_age += age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm,"
              f" {self.plant_age} days old")


def main() -> None:

    plant_list: list[Plant] = []

    print("=== Plant Factory Output ===")
    plant_list.append(Plant("Rose", 25.0, 30))
    plant_list.append(Plant("Oak", 200.0, 365))
    plant_list.append(Plant("Cactus", 5.0, 90))
    plant_list.append(Plant("Sunflower", 80.0, 45))
    plant_list.append(Plant("Fern", 15.0, 120))

    for plant in plant_list:
        print("Created: ", end='')
        plant.show()


if __name__ == "__main__":
    main()

class Plant:
    '''A Plant class that stores information about a plant.
    Attributes:
        name (str): The name of the plant.
        height (float): The height of the plant in centimeters.
        plant_age (int): The age of the plant in days.
    Methods:
        show(): Prints the plant's information in a formatted string.
        get_height(): Returns the height of the plant.
        set_height(): Sets the height of the plant in a secure manner.
        get_age(): Returns the age of the plant.
        set_age(): Sets the age of the plant in a secure manner.
    '''

    def __init__(self, name: str = "default",
                 height: float = 0.0,
                 age: int = 0) -> None:
        self.name = name
        self.set_height(height)
        self._initial_height = self._height
        self.set_age(age)

    def grow(self, height: float) -> None:
        self._height += height
        self.total_height = self._height - self._initial_height

    def age(self, age: int = 1) -> None:
        self._plant_age += age

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._plant_age} days old")

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if (height >= 0):
            self._height = height
        elif (height < 0):
            print("Error, height can't be negative")

    def get_age(self) -> int:
        return self._plant_age

    def set_age(self, age: int) -> None:
        if (age >= 0):
            self._plant_age = age
        elif (age < 0):
            print("Error, age can't be negative")


def main() -> None:
    print("=== Garden Security System ===")

    rose: Plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end='')
    rose.show()

    rose.set_height(25.0)
    print(f"\nHeight updated: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days\n")

    print(f"{rose.name.capitalize()}: ", end='')
    rose.set_height(-1.0)
    print("Height update rejected\n")
    print(f"{rose.name.capitalize()}: ", end='')
    rose.set_age(-1)
    print("Age update rejected\n")

    print("Current state: ", end='')
    rose.show()


if __name__ == "__main__":
    main()

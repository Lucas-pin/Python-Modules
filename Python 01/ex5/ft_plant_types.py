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
        print(f"{self.name}: {round(self._height, 2)}cm,"
              f" {self._plant_age} days old")

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


class Flower(Plant):

    '''A Flower class that inherits from the Plant class and adds additional
    attributes and methods specific to flowers.
    Attributes:
        color (str): The color of the flower.
        bloom (bool): A boolean indicating if the flower is blooming or not.
    Methods:
        bloom(): Sets the bloom attribute to True,
        indicating that the flower is blooming.
    Overrides Methods:
        show(): Overrides the show method from the Plant class to include
        additional information about the flower's color and bloom status.'''

    def __init__(self, name: str = "default",
                 height: float = 0.0,
                 age: int = 0,
                 color: str = "default"):
        super().__init__(name, height, age)
        self._color = color
        self._bloom = False

    def bloom(self) -> None:
        self._bloom = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if (self._bloom):
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):

    '''A Tree class that inherits from the Plant class and adds additional
    attributes and methods specific to trees.
    Attributes:
        trunk_diameter (float): The diameter of tree's trunk in centimeters.
    Methods:
        produce_shade(): Prints information about the tree's shade.
    Overrides Methods:
        show(): Overrides the show method from the Plant class to include
        additional information about the tree's trunk diameter.'''

    def __init__(self, name: str = "default",
                 height: float = 0.0,
                 age: int = 0,
                 trunk_diameter: float = 0):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):

    '''A Vegetable class that inherits from the Plant class and adds additional
    attributes and methods specific to vegetables.
    Attributes:
        harvest_season (str): The season when the vegetable will be harvested.
        nutritional_value (int): The nutritional value of the vegetable.
    Overrides Methods:
        age(): Increases the age of the vegetable and
        updates its nutritional value.
        show(): Overrides the show method from the Plant class to include
        additional information about the vegetable's
        harvest season and nutritional value.'''

    def __init__(self, name: str = "default",
                 height: float = 0.0,
                 age: int = 0,
                 harvest_season: str = "default",
                 nutritional_value: int = 0):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def age(self, age: int = 1) -> None:
        super().age(age)
        self._nutritional_value += age

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season.capitalize()}")
        print(f" Nutritional value: {self._nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("===Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    flower.bloom()
    flower.show()
    print("\n===Tree")
    tree = Tree("Oak", 200.0, 365, 5.00)
    tree.show()
    tree.produce_shade()
    print("\n===Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April")
    vegetable.show()
    vegetable.grow(42.0)
    vegetable.age(20)
    vegetable.show()


if __name__ == "__main__":
    main()

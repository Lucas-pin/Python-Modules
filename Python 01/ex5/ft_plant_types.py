class Plant:
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
        if (height > 0):
            self._height = height
        elif (height < 0):
            raise ValueError("Error, height can't be negative")

    def get_age(self) -> int:
        return self._plant_age

    def set_age(self, age: int) -> None:
        if (age > 0):
            self._plant_age = age
        elif (age < 0):
            raise ValueError("Error, age can't be negative")


class Flower(Plant):
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

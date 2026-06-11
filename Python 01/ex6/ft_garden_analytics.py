class Plant:
    def __init__(self, name: str = "default",
                 height: float = 0.0,
                 age: int = 0) -> None:
        self.name = name
        self.set_height(height)
        self._initial_height = self._height
        self.set_age(age)
        self.stats = self._Statistics()

    def grow(self, height: float) -> None:
        self.stats.register_grow()
        self._height += height
        self.total_height = self._height - self._initial_height

    def age(self, age: int = 1) -> None:
        self.stats.register_age()
        self._plant_age += age

    def show(self) -> None:
        self.stats.register_show()
        print(f"{self.name}: {round(self._height, 2)}cm,"
              f" {self._plant_age} days old")

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if (height >= 0):
            self._height = height
        elif (height < 0):
            raise ValueError("Error, height can't be negative")

    def get_age(self) -> int:
        return self._plant_age

    def set_age(self, age: int) -> None:
        if (age >= 0):
            self._plant_age = age
        elif (age < 0):
            raise ValueError("Error, age can't be negative")
    
    @staticmethod
    def check_age(age: int) -> bool:
        return age > 365
    
    @classmethod
    def anonymous(cls):
        return cls (name = "Unknown plant",
                    height = 0.0,
                    age = 0)

    class _Statistics:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def register_grow(self) -> None:
            self._grow_calls += 1

        def register_age(self) -> None:
            self._age_calls += 1

        def register_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print (f"Stats: {self._grow_calls} grow, "
                    f"{self._age_calls} age, "
                    f"{self._show_calls} show")

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
        self.stats: Tree._Statistics
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self.stats.register_produce_shade()
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    class _Statistics(Plant._Statistics):
        def __init__(self):
            super().__init__()
            self._produce_shade_calls = 0

        def register_produce_shade(self) -> None:
            self._produce_shade_calls += 1

        def display(self) -> None:
            super().display()
            print (f" {self._produce_shade_calls} shade")


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

class Seeds(Flower):
    def __init__(self, name: str = "default",
                 height: float = 0.0,
                 age: int = 0,
                 color: str = "default"):
        super().__init__(name, height, age, color)
        self._seeds_number = 0
    
    def set_seeds_number(self, seeds_number: int):
        if (self._bloom):
            self._seeds_number = seeds_number
        else:
            print(f"Error, {self.name} has not bloomed yet, can't set seeds number")
    
    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds_number}")

def display_stats(entity):
    entity.stats.display()

def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
    
    print("\n=== Flower")
    rose = Flower(name="Rose", height=15.0, age=10, color="red")
    rose.show()
    display_stats(rose)
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree(name="Oak", height=200.0, age=3650, trunk_diameter=5.0)
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)

    print("\n=== Seeds")
    sunflower = Seeds(name="Sunflower", height=80.0, age=45, color="yellow")
    sunflower.show()
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.set_seeds_number(42)
    sunflower.show()
    display_stats(sunflower)

    print("\n=== Anonymous")
    unknown_plant = Plant.anonymous()
    unknown_plant.show()
    display_stats(unknown_plant)


if __name__ == "__main__":
    main()
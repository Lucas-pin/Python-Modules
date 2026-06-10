class Plant:
    def __init__(self, name: str = "default",
                 height: float = 0.0,
                 age: int = 0) -> None:
        self.name = name
        self.set_height(height)
        self._initial_height = self._height
        self.set_age(age)
        self._statistics = self._Statistics()

    def grow(self, height: float) -> None:
        self._statistics.register_grow()
        self._height += height
        self.total_height = self._height - self._initial_height

    def age(self, age: int = 1) -> None:
        self._statistics.register_age()
        self._plant_age += age

    def show(self) -> None:
        self._statistics.register_show()
        print(f"{self.name}: {round(self._height, 2)}cm,"
              f" {self._plant_age} days old")

    def display_statistics(self) -> None:
        print(self._statistics.display())

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
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def register_grow(self) -> None:
            self.__grow_calls += 1

        def register_age(self) -> None:
            self.__age_calls += 1

        def register_show(self) -> None:
            self.__show_calls += 1

        def display(self) -> str:
            return (f"Statistics -> grow(): {self.__grow_calls}, "
                    f"age(): {self.__age_calls}, "
                    f"show(): {self.__show_calls}")

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
        self._statistics = self._TreeStatistics()
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._statistics.register_produce_shade()
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    class _TreeStatistics(Plant._Statistics):
        def __init__(self):
            super().__init__()
            self.__produce_shade_calls = 0

        def register_produce_shade(self) -> None:
            self.__produce_shade_calls += 1

        def display(self) -> str:
            base_stats = super().display()
            return (f"{base_stats}, "
                    f"produce_shade(): {self.__produce_shade_calls}")


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


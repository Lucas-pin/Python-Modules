class Plant:
    def __init__(self, name: str = "default",
                 height: float = 0.0,
                 age: int = 0) -> None:
        self._init = True
        self._height = 0
        self._initial_height = 0
        self._plant_age = 0
        self._name = name

        try:
            self._height = self.set_height(height)
            self._initial_height = self.set_height(height)
            self._plant_age = self.set_age(age)
        except ValueError as error:
            print(f"{self.name}: {error}")

    def grow(self, height: float) -> None:
        self._height += self.set_height(height)
        self.total_height = self.height - self.initial_height

    def age(self, age: int = 1):
        self._plant_age += age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm,"
              f" {self.plant_age} days old")

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if (height > 0 and height != self._height):
            self._height = height
            print(f"Height updated: {self._height}cm")
        elif (height < 0):
            print("Height update rejected")
            raise ValueError("Error, height can't be negative")

    def get_age(self) -> int:
        return self._plant_age

    def set_age(self, age: int) -> None:
        if (age > 0 and self._plant_age != age):
            self._plant_age = age
            print(f"Age updated: {self._height}days")
        elif (age < 0):
            print("Age update rejected")
            raise ValueError("Error, age can't be negative")

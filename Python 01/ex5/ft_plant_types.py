class Plant:
    def __init__(self, name: str = "default",
                 height: float = 0.0,
                 age: int = 0) -> None:
        self._init = True
        self._height = 0.0
        self._plant_age = 0
        self.name = name

        try:
            self.set_height(height)
            self.set_height(height)
            self.set_age(age)
        except ValueError as error:
            print(f"{self.name}: {error}")

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 2)}cm,"
              f" {self._plant_age} days old")

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if (height > 0 and height != self._height):
            self._height = height
        elif (height < 0):
            raise ValueError("Error, height can't be negative")

    def get_age(self) -> int:
        return self._plant_age

    def set_age(self, age: int) -> None:
        if (age > 0 and self._plant_age != age):
            self._plant_age = age
        elif (age < 0):
            raise ValueError("Error, age can't be negative")

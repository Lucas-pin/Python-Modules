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
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._plant_age} days old")

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


def main() -> None:
    print("=== Garden Security System ===")

    try:
        rose: Plant = Plant("Rose", 15.0, 10)
        print("Plant created: ", end='')
        rose.show()
    except ValueError as error:
        print(f"Plant creation rejected: {error}")

    try:
        rose.set_height(25.0)
        print(f"Height updated: {rose.get_height()}cm\n")
        rose.set_height(-1.0)
        print(f"Height updated: {rose.get_height()}cm\n")
    except ValueError as error:
        print(f"{rose.name.capitalize()}: {error}")
        print("Height update rejected\n")

    try:
        rose.set_age(30)
        print(f"Age updated: {rose.get_age()}days\n")
        rose.set_age(-1)
        print(f"Age updated: {rose.get_age()}days\n")
    except ValueError as error:
        print(f"{rose.name.capitalize()}: {error}")
        print("Age update rejected\n")

    print("Current state: ", end='')
    rose.show()


if __name__ == "__main__":
    main()

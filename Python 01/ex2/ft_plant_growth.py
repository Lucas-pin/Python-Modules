class Plant:
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
    rose: Plant = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow(0.8)
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.total_height, 2)}cm")


if __name__ == "__main__":
    main()

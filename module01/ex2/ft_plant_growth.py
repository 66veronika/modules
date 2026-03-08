class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self) -> None:
        self.height += 1

    def age_plant(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(self)


def main() -> None:
    print("=== Day 1 ===")
    rose = Plant("Rose", 25, 30)
    rose.get_info()
    start_height = rose.height
    for i in range(1, 7):
        rose.grow()
        rose.age_plant()
    print("=== Day 7 ===")
    rose.get_info()
    print(F"Growth this week: +{rose.height - start_height}cm")


if __name__ == "__main__":
    main()

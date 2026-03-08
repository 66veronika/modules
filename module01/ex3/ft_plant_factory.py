class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days old)"


def main() -> None:
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    plants = []
    for name, height, age in plant_data:
        plants.append(Plant(name, height, age))
    for plant in plants:
        print(f"Created: {plant}")
    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()

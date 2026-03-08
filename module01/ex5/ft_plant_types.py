class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")

    def __str__(self) -> str:
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_d: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_d

    def produce_shade(self) -> None:
        shade = int(3.14159265359 * ((self.trunk_diameter / 10) ** 2))
        print(f"{self.name} provides {shade} square meters of shade")

    def __str__(self) -> str:
        return (f"\n{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, heigh: int, age: int,
                 season: str, nutr: int) -> None:
        super().__init__(name, heigh, age)
        self.harvest_season = season
        self.nutritional_value = nutr

    def show_nutrition(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

    def __str__(self) -> str:
        return (f"\n{self.name} (Vegetable): {self.height}cm, "
                f"{self.age} days, {self.harvest_season} harvest")


def main() -> None:
    print("=== Garden Plant Types ===\n")
    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Daisy", 4, 29, "white")
    ]
    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Willow", 1500, 9721, 201)
    ]
    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Lettuce", 15, 72, "summer", "vitamin A")
    ]
    for flower in flowers:
        print(flower)
        flower.bloom()

    for tree in trees:
        print(tree)
        tree.produce_shade()

    for veg in vegetables:
        print(veg)
        veg.show_nutrition()


if __name__ == "__main__":
    main()

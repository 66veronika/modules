class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, amount: int = 1) -> None:
        """Grow the plant by some amount"""
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def bloom(self) -> None:
        print(f"{self.name} is blooming!")

    def __str__(self) -> str:
        status = "blooming" if self.blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        return f"{super().__str__()}, Prize points: {self.prize_points}"


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def show_plants(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print("-", plant)


class GardenManager:
    total_gardens = 0

    def __init__(self):
        self.gardens = []

    def add_garden(self, garden):
        self.gardens.append(garden)
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {cls.total_gardens}")

    class GardenStats:

        @staticmethod
        def count_plants(garden):
            return len(garden.plants)

        @staticmethod
        def total_growth(garden):
            total = 0
            for plant in garden.plants:
                total += plant.height
            return total


def main():
    print("=== Garden Management System Demo ===\n")

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    manager = GardenManager()
    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    alice_garden.grow_all()

    alice_garden.show_plants()

    stats = GardenManager.GardenStats()
    print(
        f"Plants added: {stats.count_plants(alice_garden)}, "
        f"Total growth: {stats.total_growth(alice_garden)}cm"
    )

    GardenManager.create_garden_network()


if __name__ == "__main__":
    main()

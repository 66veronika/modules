class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager():
    def __init__(self):
        self.plants = []

    def add_plant(self, plant: str) -> None:
        if plant == "":
            raise PlantError("Plant name cannot be empty!")

        self.plants.append(plant)
        print(f"Added {plant} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: str,
                           water_level: int, sunlight_hours: int) -> None:
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")

        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             f"is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             f"is too high (max 12)")

        print(f"{plant}: healthy (water: {water_level},"
              f" sun: {sunlight_hours})")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    garden = GardenManager()
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato")
        garden.add_plant("lettuce")
        garden.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    garden.water_plants()

    print("\nChecking plant health...")

    plants = [
        ("tomato", 5, 8),
        ("lettuce", 15, 8)
    ]

    for plant, water, sun in plants:
        try:
            garden.check_plant_health(plant, water, sun)
        except ValueError as e:
            print(f"Error checking {plant}: {e}")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


test_garden_management()

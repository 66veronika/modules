
def water_plants(plant_list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print("Closing watering system (cleanup)\n")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plants = {"tomato", "lettuce", "carrots"}
    water_plants(plants)
    print("Watering completed successfully!")

    print("Testing with error...")
    plants_with_E = {"tomato", None, "carrots"}
    water_plants(plants_with_E)

    print("Cleanup always happens, even with errors!")


test_watering_system()

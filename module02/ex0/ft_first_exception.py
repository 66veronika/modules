
def check_temperature(temp_str):
    try:
        temp = int(temp_str)

        if temp > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
            return None
        elif temp < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
            return None
        else:
            print(f"Temperature {temp_str}°C is perfect for plants!")
            return temp

    except ValueError:
        print(f"Error: '{temp_str}'")
        return None


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-50"]
    for t in tests:
        print(f"\nTesting temparature: {t}")
        check_temperature(t)
    print("\nAll tests completed - program didn't crash!")


test_temperature_input()

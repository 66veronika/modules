def garden_operations() -> None:
    print("Testing ValueErrors...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e} \n")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        stringvar = "missing\\_plant"
        plants = {"rose": 1, "tulip": 2, "orchid": 3}
        plants[stringvar]
    except KeyError as e:
        print(f"Caught KeyError: {e.args[0]}\n")

    print("Testing multiple errors together...")
    try:
        int("abc")
        10 / 0
        open("missing.txt")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


test_error_types()

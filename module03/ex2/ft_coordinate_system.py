import math


def distance(pos1: tuple, pos2: tuple) -> float:
    """Calculating distance using the 3D Euclidean distance formula"""
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coordin: str) -> tuple:
    try:
        x, y, z = map(int, coordin.split(","))
        return (x, y, z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
        raise


def unpacking(player: tuple, coordinates: tuple) -> None:
    print("Unpacking demonstration:")
    px, py, pz = player
    cx, cy, cz = coordinates
    print(f"Player at x={px}, y={py}, z={pz}")
    print(f"Coordinates: X={cx}, Y={cy}, Z={cz}")


def main() -> None:
    print("=== Game Coordinate System ===\n")

    pos0 = (0, 0, 0)
    pos1 = (10, 20, 5)

    print(f"Position created: {pos1}")
    print(f"Distance between {pos0} and {pos1}: {distance(pos0, pos1):.2f}\n")

    good_coords = "3,4,0"
    print(f"Parsing coordinates: \"{good_coords}\"")
    try:
        parsed_good = parse_coordinates(good_coords)
        print(f"Parsed position: {parsed_good}")
        print(f"Distance between {pos0} and {parsed_good}: "
              f"{distance(pos0, parsed_good):.1f}\n")
    except ValueError:
        pass

    bad_coords = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{bad_coords}\"")
    try:
        parsed_bad = parse_coordinates(bad_coords)
        print(f"Parsed position: {parsed_bad}")
        print(f"Distance between {pos0} and {parsed_bad}: "
              f"{distance(pos0, parsed_bad):.1f}\n")
    except ValueError:
        pass

    unpacking(parsed_good, parsed_good)


if __name__ == "__main__":
    main()

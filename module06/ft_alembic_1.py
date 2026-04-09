# ft_alembic_1.py will use the from ... import ... structure to access
# elements.py directly and then create water.

from elements import create_water


def main() -> None:
    print("=== Alembic 1 ===\n")
    print("Using: 'from ... import ...' structure to access elements.py")
    print("Testing create_water:", create_water())


if __name__ == "__main__":
    main()

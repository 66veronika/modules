#  ft_alembic_5.py will use the from alchemy import ... structure to access
# the alchemy module and then create air.

from alchemy import create_air


def main() -> None:
    print("=== Alembic 5 ===\n")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print("Testing create_air:", create_air())


if __name__ == "__main__":
    main()

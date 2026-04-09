#  ft_alembic_3.py will use the from ... import ... structure to
# access alchemy/elements.py directly and then create air

from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===\n")
    print("Accessing alchemy/elements.py using 'from ... "
          "import ...' structure")
    print("Testing create_air:", create_air())


if __name__ == "__main__":
    main()

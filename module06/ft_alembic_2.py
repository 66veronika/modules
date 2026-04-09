# ft_alembic_2.py will use the import ... structure to access
# alchemy/elements.py directly and then create earth.

import alchemy.elements


def main() -> None:
    print("=== Alembic 2 ===\n")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth:", alchemy.elements.create_earth())


if __name__ == "__main__":
    main()

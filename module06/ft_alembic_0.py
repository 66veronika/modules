# ft_alembic_0.py will use the import ... structure to access elements.py
# directly and then create fire.

import elements


def main() -> None:
    print("=== Alembic 0 ===\n")
    print("Using: 'import ...' structure to access elements.py")
    print("Testing create_fire:", elements.create_fire())


if __name__ == "__main__":
    main()

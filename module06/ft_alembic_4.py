# ft_alembic_4.py will use import alchemy to access the alchemy module and then
# create air. The create_earth() function will not be exposed through the
# module interface and raise an exception when called (you can catch the
# exception or not, this is only for pedagogical purposes). A mypy error
# will also raise, again, on purpose.

import alchemy


def main() -> None:
    print("=== Alembic 4 ===\n")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air:", alchemy.create_air())

    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    # Testing hidden function
    print("Testing the hidden create_earth:", alchemy.create_earth())


if __name__ == "__main__":
    main()

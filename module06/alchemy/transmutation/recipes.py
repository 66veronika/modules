# Absolute import
from elements import create_fire
# Relative import
from ..potions import strength_potion
from ..elements import create_air


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead toGold: brew ’{create_air()}’ and "
            f"’{strength_potion()}’ mixed with ’{create_fire()}’")

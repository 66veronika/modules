from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        # return reduce(lambda acc, item: acc + item, spells)
        return reduce(add, spells)
    elif operation == "multiply":
        # return reduce(lambda acc, item: acc * item, spells)
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(lambda mx, cur: cur if cur > mx else mx, spells)
    elif operation == "min":
        return reduce(lambda mn, cur: cur if cur < mn else mn, spells)
    else:
        raise ValueError(f"Unknown operation: '{operation}")


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Enchanting {target} with {element} (Power: {power})"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """ takes    power: int, element: str, target: str) -> str   """

    fire_enchant = partial(base_enchantment, 50, "Fire")
    ice_enchant = partial(base_enchantment, 50, "Ice")
    lightning_enchant = partial(base_enchantment, 50, "Lightning")

    return {"fire": fire_enchant, "ice": ice_enchant,
            "lightning": lightning_enchant}


@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return (f"Multi-cast: {len(spell)} "
                f"{'spells' if len(spell) > 1 else 'spell'}")

    return cast


spells: list[int] = [40, 30, 20, 10]
print("Testing spell reducer...")
print(f"Sum: {spell_reducer(spells, "add")}")
print(f"Product: {spell_reducer(spells, "multiply")}")
print(f"Max: {spell_reducer(spells, "max")}")
print(f"Min: {spell_reducer(spells, "min")}")

print()

print("Testing spell dispatcher...")
spell = spell_dispatcher()
print(spell(42))
print(spell("fireball"))
print(spell([1, 2, 3]))
print(spell({}))

 


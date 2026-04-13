from typing import List, Tuple
# from ex0.creature import Creature
from ex0.factory import CreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy
)
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    creatures_with_strategies = []
    for factory, strategy in opponents:
        creatures_with_strategies.append((factory.create_base(), strategy))

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            print("\n* Battle *")
            print(f"{c1.describe()}\n vs. \n{c2.describe()}\n now fight!")

            try:
                strategy1.act(c1)
                strategy2.act(c2)

            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def describe_opponents(opponents:
                       List[Tuple[CreatureFactory, BattleStrategy]]) -> str:
    result = []

    for factory, strategy in opponents:
        creature = factory.create_base()

        creature_name = creature.name
        strategy_name = strategy.__class__.__name__.replace("Strategy", "")

        result.append(f"{creature_name}+{strategy_name}")

    return "[ " + ", ".join(f"({r})" for r in result) + " ]"


def main() -> None:
    print("Tournament 0 (basic)")
    opponents0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    print(describe_opponents(opponents0))
    battle(opponents0)

    print("\nTournament 1 (error)")
    opponents1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    print(describe_opponents(opponents1))
    battle(opponents1)

    print("\nTournament 2 (multiple)")
    opponents2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    print(describe_opponents(opponents2))
    battle(opponents2)


if __name__ == "__main__":
    main()

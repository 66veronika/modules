from ex0 import AquaFactory, FlameFactory
from ex0.factory import CreatureFactory


def testing_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    for creature in [base, evolved]:
        print(creature.describe())
        print(creature.attack())


def testing_battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    """
    Makes base Creatures from two different factories fight.
    """
    c1 = f1.create_base()
    c2 = f2.create_base()

    print(f"{c1.describe()}\n vs.\n{c2.describe()}\n fight!")

    print(c1.attack())
    print(c2.attack())


def main() -> None:
    try:
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()
        print("Testing fire factory")
        testing_factory(flame_factory)
        print("\nTesting aqua factory")
        testing_factory(aqua_factory)
        print("\nTesting battle")
        testing_battle(flame_factory, aqua_factory)
    except Exception as e:
        print(f"An error occurred during the simulation: {e}")


if __name__ == "__main__":
    main()

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing() -> None:
    print("Testing Creature with healing capability")
    heal_factory = HealingCreatureFactory()

    for label, creature in [
        ("base", heal_factory.create_base()),
        ("evolved", heal_factory.create_evolved())
    ]:
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        print(creature.heal())


def test_transform() -> None:
    print("\nTesting Creature with transform capability")
    transform_factory = TransformCreatureFactory()

    for label, creature in [
        ("base", transform_factory.create_base()),
        ("evolved", transform_factory.create_evolved())
    ]:
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


def main() -> None:
    test_healing()
    test_transform()


if __name__ == "__main__":
    main()

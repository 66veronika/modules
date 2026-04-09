import alchemy


def main() -> None:
    print("=== Distillation 1 ===\n")
    print("Using: 'import alchemy' structure to access potions")
    print("Testing strength_potion:", alchemy.potions.strength_potion())
    print("Testing heal alias:", alchemy.heal())


if __name__ == "__main__":
    main()

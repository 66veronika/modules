import alchemy


def main() -> None:
    print("=== Transmutation 2 ===\n")
    print("Import alchemy module only")
    print(f"Testing lead to gold: "
          f"{alchemy.transmutation.recipes.lead_to_gold()}")


if __name__ == "__main__":
    main()

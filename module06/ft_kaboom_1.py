print("=== Kaboom 1 ===\n")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")


def main() -> None:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(f"Testing record dark spell: "
          f"{dark_spell_record("Fantasy", "Earth, wind and fire")}")


if __name__ == "__main__":
    main()

def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice_set = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    print(f"Player alice achievements: {alice_set}")

    bob_set = {"first_kill", "level_10", "boss_slayer", "collector"}
    print(f"Player bob achievements: {bob_set}")

    charlie_set = {"level_10", "treasure_hunter", "boss_slayer",
                   "speed_demon", "perfectionist"}
    print(f"Player charlie achievements: {charlie_set}")

    print("\n=== Achievement Analytics ===")

    uniq = alice_set.union(bob_set, charlie_set)
    print(f"All unique achievements: {uniq}")
    print(f"Total unique achievements: {len(uniq)}\n")

    common = alice_set.intersection(bob_set, charlie_set)
    print(f"Common to all players: {common}")

    rare = (
        (alice_set - bob_set - charlie_set) |
        (bob_set - alice_set - charlie_set) |
        (charlie_set - alice_set - bob_set)
    )
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice_set & bob_set}")
    print(f"Alice unique: {alice_set - bob_set}")
    print(f"Bob unique: {bob_set - alice_set}")


if __name__ == "__main__":
    main()

from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (
            spell1(target, power),
            spell2(target, power)
        )

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amplified_spell(target: str, power: int) -> str:
        return (base_spell(target, power * multiplier))

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def condition_if_valid(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return condition_if_valid


def spell_sequence(spells: list[Callable]) -> Callable:

    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def damage_spell(target: str, power: int) -> int:
    return power


def main() -> None:

    print("--- Testing spell combiner ---")
    combined = spell_combiner(fireball, heal)
    result1, result2 = combined("Dragon", 10)
    print(f"Combined spell result: {result1}, {result2}")

    print("\n--- Testing power amplifier ---")
    mega_damage = power_amplifier(damage_spell, 3)
    original = damage_spell("Dragon", 10)
    amplified = mega_damage("Dragon", 10)
    print(f"Original: {original}, Amplified: {amplified}")

    print("\n--- Testing conditional caster ---")
    strong_only = conditional_caster(
        lambda t, p: p > 20,
        fireball
    )
    print(f"Power 30: {strong_only('Dragon', 30)}")
    print(f"Power 10: {strong_only('Dragon', 10)}")

    print("\n--- Testing spell sequence ---")
    combo = spell_sequence([fireball, heal])
    print(combo("Dragon", 15))


if __name__ == "__main__":
    main()

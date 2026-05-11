from typing import Callable, Any


def mage_counter() -> Callable:
    times: int = 0

    def time_counter() -> int:
        nonlocal times

        times += 1

        return times
    return time_counter


def spell_accumulator(initial_power: int) -> Callable:
    base: int = initial_power

    def accum(power: int) -> int:
        nonlocal base

        base += power

        return base
    return accum


def enchantment_factory(enchantment_type: str) -> Callable:

    def applifier(item_name: str) -> str:
        return enchantment_type + " " + item_name

    return applifier


def memory_vault() -> dict[str, Callable]:
    common_dict: dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        common_dict[key] = value

    def recall(key: Any) -> Any:
        if key not in common_dict:
            return "Memory not found"
        return common_dict[key]

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print()

    print("Testing spell accumulator...")
    spell_100 = spell_accumulator(100)
    print(f"Base 100, add 20: {spell_100(20)}")
    print(f"Base 100, add 30: {spell_100(30)}")

    print()

    print("Testing enchantment factory...")
    flaming_factory = enchantment_factory("Flaming")
    freeze_factory = enchantment_factory("Frozen")
    print(flaming_factory("Sword"))
    print(freeze_factory("Shield"))

    print()

    print("Testing memory vault...")
    memory = memory_vault()
    print("Store 'secret' = 42")
    memory["store"]("secret", 42)
    print(f"Recall 'secret': {memory["recall"]("secret")}")
    print(f"Recall 'unknown': {memory["recall"]("unknown")}")


if __name__ == "__main__":
    main()

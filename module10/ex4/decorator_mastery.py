from typing import Callable, Any
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print("Testing spell timer...")
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            pwr = kwargs.get('power')
            if pwr is None:
                if len(args) > 2:
                    pwr = args[2]
                elif len(args) > 0:
                    pwr = args[0]
            if pwr is not None and pwr >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for current_attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if current_attempt == max_attempts:
                        print("Spell casting failed "
                              "after max_attempts attempts")
                    else:
                        print(f"Spell failed, retrying... "
                              f"(attempt {current_attempt}/{max_attempts})")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.665)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def wrong_func() -> None:
    raise ValueError


@retry_spell(max_attempts=3)
def right_func() -> None:
    print("Waaaaaaagh spelled !")


def main() -> None:
    print(f"Result: {fireball()}")
    print()

    print("Testing retrying spell...")
    wrong_func()
    right_func()

    print()

    print("Testing MageGuild...")
    mg = MageGuild()
    print(MageGuild.validate_mage_name("ilka"))
    print(MageGuild.validate_mage_name("      "))
    print(mg.cast_spell("Lightning", 15))
    print(mg.cast_spell("Lightning", -67))


if __name__ == "__main__":
    main()

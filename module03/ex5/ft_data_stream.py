from typing import Generator
import time


def event_generator(n_events: int) -> Generator[str, None, None]:
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, n_events + 1):
        player = players[i % 3]
        level = (i * 3) % 15 + 1
        action = actions[i % 3]
        yield (i, player, level, action)


def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def primes(n: int) -> Generator[int, None, None]:
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n ")
    n_events = 1000
    print(f"Processing {n_events} game events...")

    total = 0
    high_level = 0
    treasure = 0
    level_up = 0

    events = event_generator(n_events)

    start_time = time.time()
    for event_id, player, level, action in events:
        total += 1

        # print first 3 events only
        if event_id <= 3:
            print(f"Event {event_id}: Player {player} "
                  f"(level {level}) {action}")

        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasure += 1
        if action == "leveled up":
            level_up += 1
    end_time = time.time()
    print("...")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10):",
          ", ".join(str(n) for n in fibonacci(10)))
    print("Prime numbers (first 5):", ", ".join(str(p) for p in primes(5)))


if __name__ == "__main__":
    main()

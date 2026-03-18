import sys


def main() -> None:
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        for arg in range(1, len(sys.argv)):
            print(f"Argument {arg}: {sys.argv[arg]}")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()

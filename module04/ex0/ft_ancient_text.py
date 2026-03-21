
def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file_name = "ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vault: {file_name}")
        with open(file_name, "r") as f:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            for x in f:
                print(x, end="")
        print("\n\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    main()

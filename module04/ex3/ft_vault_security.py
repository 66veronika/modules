def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as f:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            for line in f:
                print(line, end="")
            print()
        with open("secure_log.txt", "w") as f:
            entry = "[CLASSIFIED] New security protocols archived\n"
            print()
            print("SECURE PRESERVATION:")
            f.write(entry)
            print(entry, end="")
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")
    except OSError as e:
        print(f"Caught an error: {e}")


if __name__ == "__main__":
    main()

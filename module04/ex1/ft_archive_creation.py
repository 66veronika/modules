def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    file_name = "new_discovery.txt"
    print(f"Initializing new storage unit: {file_name}")
    try:
        with open(file_name, "w") as f:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            entries = [
                "[ENTRY 001] New quantum algorithm discovered",
                "[ENTRY 002] Efficiency increased by 347%",
                "[ENTRY 003] Archived by Data Archivist trainee"
            ]
            for x in entries:
                print(x)
                f.write(f"{x}\n")
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")
    except OSError as e:
        print(f"Caught an error: {e}")


if __name__ == "__main__":
    main()

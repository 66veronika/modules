import os
try:
    from dotenv import load_dotenv
except ImportError:
    print("[FATAL] python-dotenv is not installed.")
    print("Install it with: pip install python-dotenv")
    exit(1)

# API_KEY = "dbsuiosd"
# DATABASE_URL = 'neo'


def check_security(script_path: str) -> None:
    with open(script_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    found_secret = False

    # We look for the variable name followed by =' or ="
    # This avoids matching os.getenv("API_KEY")
    for line in lines:
        clean_line = line.replace(" ", "").strip()

        if (
            clean_line.startswith("API_KEY='") or
            clean_line.startswith('API_KEY="') or
            clean_line.startswith("DATABASE_URL='") or
            clean_line.startswith('DATABASE_URL="')
        ):

            found_secret = True
            break

    if found_secret:
        print("[WARN] Potential hardcoded secrets detected!")
    else:
        print("[OK] No hardcoded secrets detected")


def main():
    """Load and validate system configuration from environment variables."""

    env_found = load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...")

    mode = os.getenv("MATRIX_MODE", "unknown")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_lvl = os.getenv("LOG_LEVEL", "INFO")
    zion_url = os.getenv("ZION_ENDPOINT")

    if not all([db_url, api_key, zion_url]):
        print("\n[WARNING] Configuration incomplete! Variables missing.")
        print("Ensure .env is configured or environment variables are set.")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if db_url:
        db_status = ("Connected to local instance" if "localhost" in db_url
                     else "Connected to production cluster")
    else:
        db_status = "Not configured"

    print(f"Database: {db_status}")
    print(f"API Access: {'Authenticated' if api_key else 'Access Denied'}")
    print(f"Log Level: {log_lvl}")
    print(f"Zion Network: {'Online' if zion_url else 'Offline'}")

    print("\nEnvironment security check:")
    check_security(os.path.abspath(__file__))

    env_msg = 'properly configured' if env_found else 'not found'
    print(f"[{'OK' if env_found else '!!'}] .env file {env_msg}")

    is_prod = mode == "production"
    prod_msg = 'active' if is_prod else 'available'
    print(f"[{'OK' if is_prod else '--'}] Production overrides {prod_msg}")

    if mode == "unknown":
        print("\nThe Oracle is blind without MATRIX_MODE.")
    else:
        print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()

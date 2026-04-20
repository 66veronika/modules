import sys
import os
import site


def main() -> None:
    in_venv = sys.prefix != sys.base_prefix

    if not in_venv:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")

    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        venv_path = sys.prefix
        venv_name = os.path.basename(venv_path)

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting\n"
              "the global system.\n")
        site_packages = site.getsitepackages()
        if site_packages:
            print("Package installation path:")
            print(site_packages[0])


if __name__ == "__main__":
    main()

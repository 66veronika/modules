import importlib.metadata


def check_dependencies() -> bool:
    required = ["pandas", "numpy", "matplotlib"]

    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    all_good = True

    for pkg in required:
        try:
            version = importlib.metadata.version(pkg)
            print(f"[OK] {pkg} ({version}) - ready")
        except importlib.metadata.PackageNotFoundError:
            print(f"[FAIL] {pkg} - not installed")
            all_good = False

    if not all_good:
        print("\nMissing dependencies!")
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("\nOr with Poetry:")
        print("poetry install")
        return False

    return True


def run_analysis() -> None:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    data = np.random.randn(1000)
    df = pd.DataFrame(data, columns=["values"])

    print(f"Processing {len(df)} data points...")

    plt.plot(df["values"])
    plt.title("Matrix Data")
    plt.savefig("matrix_analysis.png")

    print("Generating visualization...\n")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    if not check_dependencies():
        return
    run_analysis()


if __name__ == "__main__":
    main()

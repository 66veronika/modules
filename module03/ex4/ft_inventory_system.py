import sys


def main() -> None:
    print("=== Inventory System Analysis ===\n")

    if len(sys.argv) < 2:
        print("No inventory provided.")
        return

    inventory = {}
    for arg in sys.argv[1:]:
        try:
            name, qty = arg.split(":")
            inventory[name] = int(qty)
        except ValueError:
            print(f"Invalid input: {arg}")

    total_items = 0
    for qty in inventory.values():
        total_items += qty
    unique_items = len(inventory)

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")

    print("\n=== Current Inventory ===")
    for item, qty in inventory.items():
        percent = (qty / total_items) * 100
        print(f"{item}: {qty} units ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_item = None
    least_item = None
    most_qty = -1
    least_qty = float("inf")
    for item, qty in inventory.items():
        if qty > most_qty:
            most_qty = qty
            most_item = item
        if qty < least_qty:
            least_qty = qty
            least_item = item
    print(f"Most abundant: {most_item} ({most_qty} units)")
    print(f"Least abundant: {least_item} ({least_qty} units)")

    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}

    for item, qty in inventory.items():
        if qty >= 4:
            moderate[item] = qty
        else:
            scarce[item] = qty
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock = []
    for item, qty in inventory.items():
        if qty <= 1:
            restock.append(item)
    print(f"Restock needed: {', '.join(restock)}")

    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys:", ", ".join(inventory.keys()))
    print("Dictionary values:", ", ".join([str(v)
          for v in inventory.values()]))
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    main()

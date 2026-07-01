import sys

if len(sys.argv) >= 1:
    inventory: dict[str, int] = {}
    for item in sys.argv[1:]:
        entry = item.split(":")
        if (len(entry) < 2):
            print(f"Error - invalid parameter {item}")
            continue
        elif entry[0] in inventory.keys():
            print(f"Redundant item '{entry[0]}' - discarding")
            continue
        try:
            weapon = entry[0]
            quantity = int(entry[1])
        except (Exception) as ex:
            print(f"Quantity error for '{entry[0]}': {ex}")
            continue
        inventory[weapon] = quantity
    keys = list(inventory.keys())
    values = list(inventory.values())
    print(f"Got inventory: {inventory}")
    print(f"Total quantity of the {len(keys)} items: {sum(values)}")
    print("")

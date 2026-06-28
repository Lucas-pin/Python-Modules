import math


def get_player_pos() -> tuple[float, float, float]:
    valid = False
    while (not valid):
        values = []
        entry = input("Enter new coordinates as floats in format 'x,y,z':")
        params = [param.strip() for param in entry.split(",")]
        param_len = 0
        for param in params:
            param_len += 1
        if (param_len != 3):
            print("Invalid syntax")
            continue
        for param in params:
            try:
                values.append(float(param))
            except (Exception) as ex:
                print(f"Error on parameter {param}: {ex}")
                break
        else:
            valid = True
    x, y, z = values
    return x, y, z


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_coord = get_player_pos()
    print(f"Got a first tuple: {first_coord}")
    x1, y1, z1 = first_coord
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    distance = math.sqrt((x1)**2 + (y1)**2 + (z1)**2)
    print(f"Distance to center: {distance:.4f}\n")

    print("Get a second set of coordinates")
    second_coord = get_player_pos()
    x2, y2, z2 = second_coord

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")


if __name__ == "__main__":
    main()

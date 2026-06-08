def ft_plant_age():
    days: int = int(input("Enter plant age in days: "))
    if (days > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

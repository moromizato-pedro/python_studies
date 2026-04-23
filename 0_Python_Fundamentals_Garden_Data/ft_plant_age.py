def ft_plant_age() -> None:
    x = int(input("Enter plant age in days: "))
    if x > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant need more time to grow.")

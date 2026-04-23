def ft_count_harvest_iterative() -> None:
    x = int(input("Days until harvest: "))
    for i in range(1, x + 1):
        print(f"Day {i}")
    print("Harvest time!")

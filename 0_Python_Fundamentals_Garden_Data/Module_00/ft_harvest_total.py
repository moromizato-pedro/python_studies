def ft_harvest_total() -> None:
    x = 0
    for i in range(1, 4):
        print(f"Day {i} harvest: ", end='')
        x += int(input())
    print("Total harvest:", x)

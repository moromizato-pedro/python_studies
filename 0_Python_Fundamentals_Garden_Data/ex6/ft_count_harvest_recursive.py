def ft_count_harvest_recursive() -> None:
    x = int(input("Days until harvest: "))
    ft_count(x)
    print("Harvest time!")


def ft_count(count: int) -> None:
    if count > 0:
        ft_count(count - 1)
        print(f"Day {count}")

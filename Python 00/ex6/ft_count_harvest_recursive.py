def ft_count_harvest_recursive() -> None:
    count: int = 1
    days: int = int(input("Days until harvest: "))
    helper(count, days)
    print("Harvest time!")


def helper(count: int, days: int) -> None:
    if (count <= days):
        print(f"Day {count}")
    else:
        return
    count += 1
    helper(count, days)

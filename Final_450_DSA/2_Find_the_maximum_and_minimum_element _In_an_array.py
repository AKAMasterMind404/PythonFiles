def min_and_max(arr: list) -> tuple:
    return max(arr), min(arr)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(min_and_max(arr))

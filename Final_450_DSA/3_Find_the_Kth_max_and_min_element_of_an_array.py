def kthMax(arr: list, k: int) -> int:
    return sorted(arr)[-k]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(kthMax(arr, 1))
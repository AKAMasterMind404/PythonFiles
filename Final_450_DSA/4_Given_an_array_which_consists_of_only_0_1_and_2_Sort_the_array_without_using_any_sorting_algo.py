def arrSort(arr: list) -> list:
    return [0] * arr.count(0) + [1] * arr.count(1) + [2] * arr.count(2)


if __name__ == '__main__':
    arr = [0, 1, 0, 1, 1, 1, 0, 0, 2, 2, 2, 1, 1, 0, 0, 0, 1, 2, 0]
    print(arrSort(arr))

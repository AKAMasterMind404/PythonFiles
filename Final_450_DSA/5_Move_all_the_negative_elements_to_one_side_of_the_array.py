def moveNegatives(arr: list) -> list:
    p ,n = list(), list()
    for i in arr:
        if i >= 0:
            p.append(i)
        else:
            n.append(i)
    return p + n


if __name__ == '__main__':
    arr = [1, 2, 6, 3, 9, -4, 2, 8, 7, -6]
    print(moveNegatives(arr))

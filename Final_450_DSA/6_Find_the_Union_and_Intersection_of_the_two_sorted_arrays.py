def union(a1: list, a2: list) -> list:
    a1.sort(), a2.sort()
    return a1 + [i for i in a2 if i in a1]


def intersection(a1: list, a2: list) -> list:
    return [i for i in a1 + a2 if i in a1 and i in a2]


if __name__ == '__main__':
    x1 = [1, 1, 2, 2, 3, 3]

    x2 = [2, 2, 3, 3, 4, 4]

    print(union(x1, x2))
    print(intersection(x1, x2))

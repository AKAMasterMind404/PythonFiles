def simplify(num):
    # num = 5*(p1) + p2

    p1 = num // 5
    p2 = num % 5

    if p1 + p2 <= 5:
        return p1 + p2
    # return p1 + p2
    else:
        return simplify(p1 + p2)


def switch(digit, power):
    digit = int(str(digit)[-1])
    # print(digit)
    d = {
        1: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}, 2: {1: 2, 2: 4, 3: 8, 4: 6, 5: 2},
        3: {1: 3, 2: 9, 3: 7, 4: 1, 5: 3}, 4: {1: 4, 2: 6, 3: 4, 4: 6, 5: 4},
        5: {1: 5, 2: 5, 3: 5, 4: 5, 5: 5}, 6: {1: 6, 2: 6, 3: 6, 4: 6, 5: 6},
        7: {1: 7, 2: 9, 3: 3, 4: 1, 5: 7}, 8: {1: 8, 2: 4, 3: 2, 4: 6, 5: 8},
        9: {1: 9, 2: 1, 3: 9, 4: 1, 5: 9}
    }
    try:
        return d[digit][power]
    except KeyError:
        return 0


def last_digit(n1, n2):
    if n2 == 0: return 1
    if n1 == 10: return 0

    matters = int(str(n1)[-1])
    return switch(matters, simplify(n2))


if __name__ == '__main__':
    print(last_digit(3715290469715693021198967285016729344580685479654510946723,
                     68819615221552997273737174557165657483427362207517952651), 7)
    print(last_digit(1467457854333305658879016260777430720846780770299931501259,
                     10594321536442405328888687781986100457406255010126586441233))

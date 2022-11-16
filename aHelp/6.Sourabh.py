import math


def reverseArray(a: list):
    for i in range(math.ceil(len(a) // 2)):
        a[i], a[-1 * (i + 1)] = a[-1 * (i + 1)], a[i]
    return a


print(reverseArray([1, 5, 6, 8, 9]))

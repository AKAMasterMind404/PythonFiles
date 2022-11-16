def isSubArray(a1: list, a2: list):
    smaller = a1
    larger = a2

    if len(a1) > len(a2):
        larger, smaller = smaller, larger

    l2 = []

    for i in larger:
        if i in smaller:
            l2.append(i)

    return smaller == l2


ans = isSubArray([1, 2, 3, 4], [1, 3, 4])
print(ans)

def secondLargest(arr: list):
    lar = arr[0]

    for i in set(arr):
        if i > lar:
            lar = i

    sec = arr[0]

    for i in set(arr):
        if i > sec and i != lar:
            sec = i

    return sec


print(secondLargest([0, 0, 0, 0, 0, 1, 2]))

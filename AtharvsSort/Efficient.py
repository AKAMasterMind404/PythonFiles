# l=[1,2,3,4,5]
def removeElement(arr, element):
    fl = []
    z = 0
    while z < len(arr):
        if arr[z] != element:
            fl.append(arr[z])
        else:
            break
        z += 1
    return fl + arr[z + 1::]


def minimum(arr):
    m = arr[0]
    for i in arr:
        if i <= m:
            m = i
    return m


def atharvSort(arr):
    n = []
    while len(arr) > 0:
        n.append(min(arr))  # min() can be used
        arr = removeElement(arr, min(arr))  # remove()can be used
    return n


print(atharvSort([5, 4, 3, 2, 1]))

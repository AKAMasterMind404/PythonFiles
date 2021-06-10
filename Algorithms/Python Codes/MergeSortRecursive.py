import math

def mergeSort(array):

    if len(array) <= 1:
        return array

    mid = math.ceil(len(array) / 2)
    fh = mergeSort(array[:mid])
    sh = mergeSort(array[mid:])

    return merge(fh, sh)

def merge(l1, l2):
    p1 = 0
    p2 = 0
    srtd = []
    while len(srtd) != len(l1) + len(l2):
        if p1 == len(l1):
            srtd.append(l2[p2])
            p2 += 1
        elif p2 == len(l2):
            srtd.append(l1[p1])
            p1 += 1
        else:
            if l1[p1] > l2[p2]:
                srtd.append(l2[p2])
                p2 += 1
            else:
                srtd.append(l1[p1])
                p1 += 1
    return srtd

#print(mergeSort([5,4,3,2,1,-3,69,27,12,8,-8,5]))
#!/bin/python3
from collections import Counter

def isGP(arr,r,i,j,k):
    a=arr[i]
    ar=a*r
    ar2=a*r*r
    return ar==arr[j] and ar2==arr[k]


def countTriplets(arr, r):
    left_map = Counter()
    right_map = Counter(arr)
    count = 0
    for j in arr:
        right_map[j] -= 1
        i = left_map[j/r]
        k = right_map[j*r]
        count += i * k
        left_map[j] += 1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)
    # fptr.write(str(ans) + '\n')
    #
    # fptr.close()

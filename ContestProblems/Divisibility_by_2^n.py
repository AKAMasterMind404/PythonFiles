def calcNum2sInArr(arr):
    n_2s = 0
    d = list()

    for i in arr:
        num = 0
        while i % 2 == 0 and i > 0:
            num += 1
            i = i / 2
        n_2s += num
        d.append(num)

    return n_2s, d


for _ in range(int(input())):
    input()
    array = list(map(int, input().split()))
    l = len(array)
    __2 = calcNum2sInArr(array)
    n_2s = __2[0]

    __a = calcNum2sInArr(list(range(1, l + 1)))
    available = __a[0]
    if n_2s + available >= len(array):
        required = len(array) - n_2s
        ans = 0
        ded = sorted(__a[1])[::-1]
        for i in ded:
            if required > 0:
                ans+=1
                required -= i
        print(ans)
    else:
        print("-1")

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


a = calcNum2sInArr([20, 7, 14, 18, 3, 5])
print([20, 7, 14, 18, 3, 5])
print(a[1])
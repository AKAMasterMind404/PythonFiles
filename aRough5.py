def check(arr, k):
    for i in arr:
        for j in arr:
            if i + j == k:
                return True
    return False


print(check([10, 3, 5, 7], 17))

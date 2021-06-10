limit = 5


def fibbonacci(a, b, curr):
    global limit
    if curr < limit:
        print(a + b)
        fibbonacci(b, a + b, curr + 1)
    print("this is curr", curr)


fibbonacci(0.0, 1.0, 0)

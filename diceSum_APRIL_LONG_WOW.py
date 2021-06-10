def diceSum(num):
    h = {0: 0, 1: 20, 2: 36, 3: 51, 4: 60}

    simple = h.get(num)
    if simple: return simple

    layers = (num // 4) - 1
    tot = (44 * layers) + 60

    extra = num % 4

    tot += h.get(extra) - (4 * extra)

    return int(tot)


for _ in range(int(input())):
    print(diceSum(int(input())))

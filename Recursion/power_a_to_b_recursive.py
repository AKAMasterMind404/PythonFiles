def power(a, b):
    if b == 0: return 1

    if b > 0:
        if b == 1: return a

        return a * power(a, b - 1)

    elif b < 0:
        if b == -1: return 1 / a

        return (1 / a) * power(a, b + 1)


print(power(20, -1))

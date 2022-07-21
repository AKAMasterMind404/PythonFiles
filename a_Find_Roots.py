def findRoots(a, b, c) -> tuple:
    d = (b * b) - (4 * a * c)
    if d < 0:
        print("No roots!")
        return None, None
    else:
        num1 = -1 * b + d ** 0.5
        num2 = -1 * b - d ** 0.5
        den = 2 * a

        r1 = num1 / den
        r2 = num2 / den

    return r1, r2


if __name__ == '__main__':
    a, b, c = 1, 11, 28
    ans = findRoots(a, b, c)
    print(ans)
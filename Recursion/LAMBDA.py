# STARTED AND ENDED ON 9/4/2021
# B.Tech 3rd Year
# Atharv Karbhari

fact = lambda num: num if num in range(2) else num * fact(num - 1)
power = lambda a, b: a if b == 1 else a * power(a, b - 1)
countDigits = lambda num: 1 if 0 <= num < 10 else 1 + countDigits(num // 10)
natural = lambda a, b: (print(a, end=' '), natural(a + 1, b)) if a < b else None
naturalReverse = lambda b, a: (print(b), naturalReverse(b - 1, a)) if b >= a else None
isPallindromeString = lambda i: i == i[::-1]
armstrongNumber = lambda a, b: a ** b if 0 <= a <= 9 else armstrongNumber(a // 10, b) + (a % 10) ** b
reverseNumber = lambda n, u: n if not u else (n % 10) * (10 ** u) + reverseNumber(n // 10, u - 1)
binary = lambda a: a if a in [0, 1] else binary(a // 2) + str(a % 2)
product = lambda a, b: a if b == 1 else a + product(a, b - 1)
squareSum = lambda n: 1 if n == 1 else n ** 2 + squareSum(n - 1)
listSum = lambda li: 0 if not li else li[0] + lengthOfAList(li[1::])
stringBackwards = lambda s: s[0] if 1 == len(s) else stringBackwards(s[1::]) + s[0]
palString = lambda s: True if len(s) <= 1 else (s[0] == s[len(s) - 1] and palString(s[1:len(s) - 1]))
pal = lambda s: True if len(s) <= 1 else s[0] == s[len(s) - 1] and pal(s[1:len(s) - 1])
numPackages = lambda n, s, p: p if n - s < 0 else numPackages(n - s, s, p + 1)


def oddSum(a, b):
    if a + 2 >= b:
        return a

    if not a % 2: a += 1
    print(a)

    return a + oddSum(a + 2, b)


def evenSum(a, b, s):
    if a >= b:
        return s
    if a % 2:
        a += 1
    s += a
    return evenSum(a + 2, b, s)


def LCM(a, b, c):
    c += b
    if not ((c % a) + (c % b)): return c
    return LCM(a, b, c)


def square(n):
    if n == 1 or n == 0:
        print(n, end=' ')
    else:
        square(n - 1)
        print(n * n, end=' ')


def lengthOfAList(li):
    if not li: return 0

    return li[0] + lengthOfAList(li[1::])


def linearSearch(arr, ele, index):
    if not arr:
        return "Not Found"

    if arr[0] == ele:
        return index
    else:
        return linearSearch(arr[1::], ele, index + 1)

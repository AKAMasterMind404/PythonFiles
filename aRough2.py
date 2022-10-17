def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 6
    else:
        return (6 * (n - 1)) + f(n - 1)


for _ in range(int(input())):
    n = 10 - int(input())
    input()
    print(f(n))
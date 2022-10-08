'''
1   2   9   10  25  26
4   3   8   11  24  27
5   6   7   12  23  28
16  15  14  13  22  29
17  18  19  20  21  30
36  35  34  33  32  31
//
2 3 -> 8
4 2 -> 15
'''
def solve(y, x):
    if y > x:
        if y % 2 == 0:
            return (y ** 2) - (x - 1)
        else:
            return (y - 1) ** 2 + x
    elif x > y:
        if x % 2 == 1:
            return (x ** 2) - (y - 1)
        else:
            return (x - 1) ** 2 + y
    else:
        return (x ** 2) - (x - 1)

print(__name__)

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        y,x = map(int, input().split())
        print(solve(y, x))


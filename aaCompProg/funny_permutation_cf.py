url = 'https://codeforces.com/contest/1741'

for _ in range(int(input())):
    n = int(input())

    if n in [1, 3]:
        print('1 3 2')
    elif n == 2:
        print('2 1')
    else:
        if n % 2 == 0:
            [print(str(i), end=' ') for i in range(n, 1, -1)]
            print('1')
        else:
            m = (n + 1) // 2
            [print(str(i), end=' ') for i in range(n, m, -1)]
            [print(str(i), end=' ') for i in range(1, m)]
            print(str(m))

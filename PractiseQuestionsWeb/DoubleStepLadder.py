n = int(input())
[print(((' ' * i) + ('*' * (n - i) * 2) + (' ' * i) + '\n') * 2, end='') for i in range(n - 1, -1, -1)]

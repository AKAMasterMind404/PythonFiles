url = 'https://codeforces.com/contest/1741/problem/A'

def compare(shirt:str):
    w = {'S': 1, 'M': 2, 'L': 3}
    size = ''.join(shirt.split('X'))
    amount = w[size]
    n_x = shirt.count('X')
    return amount + (0.01 * n_x)


for _ in range(int(input())):
    a, b = input().strip().split()

    c1 = compare(a)
    c2 = compare(b)

    if c1 == c2:
        print("=")
    elif int(c1) == int(c2) == 1:
        if c1 > c2:
            print("<")
        else:
            print(">")
    else:
        if c1 > c2:
            print(">")
        else:
            print("<")
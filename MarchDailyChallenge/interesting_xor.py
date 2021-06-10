from itertools import combinations_with_replacement as comb

for _ in range(int(input())):
    c = int(input())

    d = len(bin(c)) - 2

    for i, j in list(comb(list(range(1,2**d)), 2))[::-1]:
        num = i ^ j
        if num == c:
            print(i * j)
            break

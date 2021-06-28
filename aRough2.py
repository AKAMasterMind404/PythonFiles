def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


for a in range(int(input())):
    arr = sorted(list(map(int, input().split())))
    j1, j2 = map(int, input().split())
    dec = gcd(j1, j2)
    ans = "Alive"
    for ele in arr:
        if ele and not ele % dec:
            ans = "Dead"
            break
    print(ans)

def bd(n):
    ans = 0
    pw = 1
    while n > 0:
        rem = n % 10
        n = n // 10
        ans += rem * pw
        pw = pw * 2

    return ans


def d(s):
    s1 = ''
    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u']:
            s1 += '0'
        else:
            s1 += '1'
    return bd(int(s1))


print(d(input()))
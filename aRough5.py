for _ in range(int(input())):
    s = "".join(input().split('?'))
    # print(s)
    ans = "No"
    for i in range(len(s) - 1):
        if s[i] == 'M' and s[i + 1] == 'U':
            ans = "Yes"

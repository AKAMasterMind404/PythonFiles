def solve(nums):
    s_n = 0
    s_p = 0

    for i in nums:
        if i < 0:
            s_n += abs(i)
        else:
            s_p += abs(i)

    return abs(s_p - s_n)


for _ in range(int(input())):
    # for _ in range(1):
    input()
    nums = list(map(int, input().split()))
    ans = solve(nums)
    print(ans)

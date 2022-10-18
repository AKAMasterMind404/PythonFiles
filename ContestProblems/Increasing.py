n = int(input())
for _ in range(n):
    size = int(input())
    nums = list(map(int, input().split()))
    word = list(input())

    d = {}
    isFound = False

    for i in range(len(nums)):
        if d.get(nums[i]) is None:
            d[nums[i]] = word[i]
        else:
            if d.get(nums[i]) != word[i]:
                print("NO")
                isFound = True
                break

    if not isFound:
        print("YES")

def firstNegativeNumber(arr, n, k):
    start = 0
    end = 0
    neg_nums = []
    result = []

    # start till end pointer is less then n
    while end < n:
        print(start, end)
        # If we found negative then add it to neg num list
        if arr[end] < 0:
            neg_nums.append(arr[end])

        # increase end pointer till we did not reach window size
        if (end - start + 1) < k:
            end += 1

        # if window size
        elif (end - start + 1) == k:
            # check that list of neg nums greater then 0 then add first element
            if len(neg_nums) > 0:
                result.append(neg_nums[0])
                # to remove all calc check first element with start pointer
                if arr[start] == neg_nums[0]:
                    neg_nums.pop(0)
            else:
                result.append(0)

            start += 1
            end += 1

    return result


arr = [12, -1, -7, 8, -15, 30, 18, 28]
n = len(arr)
k = 3
ans = firstNegativeNumber(arr, n, k)
print(ans)

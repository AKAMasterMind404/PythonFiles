def combineArrays(a1: list, a2: list):
    l = max(len(a1), len(a2))

    ans = []

    for i in range(l):
        if i < len(a1):
            ans.append(a1[i])
        if i < len(a2):
            ans.append(a2[i])

    return ans


ans = combineArrays([1, 2, 3], ['a', 'b', 'c', 'd', 'e'])
print(ans)

'''
The logic behind this problem is to append a
character of each list on index at a time and
when a list runs out of indices we simply keep
looping until all indices of the larger array
are covered. For this, we initialize an integer
variable to the maximum value of length of both
arrays. We then loop from 0 to this number. In
each iteration we check whether the current number
is smaller than the list of each of the arrays. If
the index is smaller, then the character is added
to an empty initialized stack. When we run out of
indices, the condition simply passes the appending
of characters to the larger array.
'''
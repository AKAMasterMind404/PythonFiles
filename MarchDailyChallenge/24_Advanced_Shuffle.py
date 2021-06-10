class Solution:
    def advantageCount(self, A: list, B: list) -> list:
        order = [i for i in range(len(B))]
        ans = [0 for _ in range(len(A))]
        order.sort(key=lambda x: -B[x])
        A.sort()
        for ix in order:
            ans[ix] = A.pop() if A[-1] > B[ix] else A.pop(0)
        return ans
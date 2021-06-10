from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, E: list) -> int:
        E.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, height in E:
            left = bisect_left(dp, height)
            if left == len(dp):
                dp.append(height)
            else:
                dp[left] = height
        return len(dp)

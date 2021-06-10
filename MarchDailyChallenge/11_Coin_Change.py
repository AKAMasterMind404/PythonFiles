class Solution:
    def coinChange(self, coins, amount):

        if not amount: return 0

        dp = [float("inf") for i in range(amount + 1)]

        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                new = [coin for coin in coins if coin < i]
                if not new:
                    dp[i] = float("inf")
                for j in new:
                    dp[i] = min(dp[i], 1 + dp[i - j])
        if dp[-1] == float("inf"):
            return -1

        return dp[-1]

class Solution:
    def pacificAtlantic(self, M: list) -> list:
        if not M: return M
        x, y = len(M[0]), len(M)
        ans, dp = [], [0] * (x * y)

        def dfs(i: int, j: int, w: int, h: int):
            ij = i * x + j
            if dp[ij] & w or M[i][j] < h: return
            dp[ij] += w
            h = M[i][j]
            if dp[ij] == 3: ans.append([i, j])
            if i + 1 < y: dfs(i + 1, j, w, h)
            if i > 0: dfs(i - 1, j, w, h)
            if j + 1 < x: dfs(i, j + 1, w, h)
            if j > 0: dfs(i, j - 1, w, h)

        for i in range(y):
            dfs(i, 0, 1, M[i][0])
            dfs(i, x - 1, 2, M[i][x - 1])
        for j in range(x):
            dfs(0, j, 1, M[0][j])
            dfs(y - 1, j, 2, M[y - 1][j])
        return ans

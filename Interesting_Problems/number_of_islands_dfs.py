class Solution:
    def occupy(self, m, n, grid):
        if m < 0 or m >= len(grid) or n < 0 or n >= len(grid[0]) or grid[m][n] == '2' or grid[m][n] == '0':
            return
        grid[m][n] = '2'
        [self.occupy(m - 1, n, grid), self.occupy(m + 1, n, grid), self.occupy(m, n - 1, grid),
         self.occupy(m, n + 1, grid)]

    def numIslands(self, grid: list):
        num_islands = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                cell = grid[m][n]
                if cell == '1':  # 1
                    num_islands += 1
                    self.occupy(m, n, grid)
        return num_islands


ans = Solution().numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])

print(ans)

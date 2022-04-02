class Solution:
    def markIslands(self, grid: list, x: int, y: int, currSet: set) -> set:
        rows = len(grid)
        cols = len(grid[0])
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return currSet

        if grid[x][y] in [0, 2]:
            return currSet

        grid[x][y] = 2
        currSet.add((x, y))
        s1 = self.markIslands(grid, x + 1, y, currSet)
        s2 = self.markIslands(grid, x - 1, y, currSet)
        s3 = self.markIslands(grid, x, y + 1, currSet)
        s4 = self.markIslands(grid, x, y - 1, currSet)
        return s1.union(s2).union(s3).union(s4)

    def countSubIslands(self, grid1: list, grid2: list) -> int:
        g1Islands = []
        g2Islands = []

        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                i1 = self.markIslands(grid1, i, j, set())
                if i1: g1Islands.append(i1)
                i2 = self.markIslands(grid2, i, j, set())
                if i2: g2Islands.append(i2)

        [print(i) for i in g1Islands]
        print()
        [print(i) for i in g2Islands]
        print()

        subislands = 0
        for island in g2Islands:
            for jland in g1Islands:
                if island.issubset(jland):
                    subislands += 1
        return subislands

ans = Solution().countSubIslands(
    [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
    [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]])

print(ans)


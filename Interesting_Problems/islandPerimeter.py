class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        def invalid(board, x, y):
            return not (0 <= x < len(board)) or not (0 <= y < len(board[x])) or board[x][y] in [0, 2]

        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cell = grid[i][j]
                if cell == 1:
                    for newI, newJ in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1], ]:
                        if invalid(grid, newI, newJ):
                            perimeter += 1

        return perimeter

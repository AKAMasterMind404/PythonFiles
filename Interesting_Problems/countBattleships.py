class Solution:
    def __init__(self):
        self.islands = 0

    def dfs(self, base: list, x, y):
        def invalid(board, x, y):
            return not (0 <= x < len(board)) or not (0 <= y < len(board[x])) or board[x][y] in [".", "O"]

        if invalid(base, x, y):
            return
        else:
            if base[x][y] == "X":
                base[x][y] = "O"
                if not invalid(base, x + 1, y):
                    self.dfs(base, x + 1, y)
                elif not invalid(base, x, y + 1):
                    self.dfs(base, x, y + 1)
                else:
                    self.islands += 1

    def countBattleships(self, board: list[list[str]]) -> int:
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.dfs(board, i, j)
        return self.islands

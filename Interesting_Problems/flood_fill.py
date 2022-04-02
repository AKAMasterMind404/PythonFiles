class Solution:
    def paint(self, image, i, j, newColor, rows, cols, source):
        if (i < 0) or (i >= rows) or (j < 0) or (j >= cols):
            return
        elif image[i][j] != source:
            return
        image[i][j] = newColor
        self.paint(image, i + 1, j, newColor, rows, cols, source)
        self.paint(image, i - 1, j, newColor, rows, cols, source)
        self.paint(image, i, j + 1, newColor, rows, cols, source)
        self.paint(image, i, j - 1, newColor, rows, cols, source)

    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        if newColor == image[sr][sc]:
            return image
        self.paint(image, sr, sc, newColor, len(image), len(image[0]), image[sr][sc]),
        return image


s1 = Solution().floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 2)
print(s1)

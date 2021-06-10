class Solution:
    def distributeCandies(self, candyType: list) -> int:
        canEat = len(candyType) // 2
        unique = len(set(candyType))

        return canEat if unique > canEat else unique

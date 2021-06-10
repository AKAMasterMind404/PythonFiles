class Solution:
    def missingNumber(self, nums: list) -> int:
        return sum(list(range(len(nums) + 1))) - sum(nums)


l1 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
s1 = Solution()
print(s1.missingNumber(l1))

class Solution:
    def findErrorNums(self, nums: list) -> list:
        hashMap = {nums[0]: 1}
        duplicate = nums[0]
        for i in range(1, len(nums)):
            if not hashMap.get(nums[i]):
                hashMap[nums[i]] = 1
            else:
                duplicate = nums[i]
                break
        nums.remove(duplicate)
        ans = sum(list(range(len(nums) + 2))) - sum(nums)  # Adding 2: removing duplicate, + 1 based range
        return [duplicate, ans]


l1 = [1, 2, 2, 4]
l2 = [3, 2, 2]
l3 = [1, 2, 3, 3, 4, 5]
l4 = [3, 2, 3, 4, 6, 5]
s1 = Solution()
print(s1.findErrorNums(l4))

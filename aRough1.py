class Solution:
    def binarySearch(self, l, h, arr, element):
        if element > arr[-1]:
            return arr[-1]
        if l > h:
            return arr[l]
        
        mid = l + (h - l) // 2
        mid_element = arr[mid]

        if mid_element == element:
            return arr[mid + 1] if mid + 1 < len(arr) else arr[-1]
        elif mid_element < element:
            return self.binarySearch(mid + 1, h, arr, element)
        else:
            return self.binarySearch(l, mid - 1, arr, element)
    
    def nextGreatestLetter(self, nums: list[int], target: int) -> int:
        return self.binarySearch(0, len(nums), nums, target)

    
s1 = Solution()
print(s1.nextGreatestLetter(["c","f","j"],"j"))
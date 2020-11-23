class Solution:
    def findMin(self, nums):
        
        low, high = 0, len(nums) - 1
​
        while (low <= high):
            if low == high:
                return nums[low]
​
            mid = low + (high - low) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            else:
                if nums[mid] > nums[high]:
                    low = mid + 1
                    continue
                elif nums[mid] < nums[low]:
                    high = mid - 1
                    continue
                return nums[low]

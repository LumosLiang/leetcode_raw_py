class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
 
        lo, hi = 0, len(nums) - 1
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
​
            if hi - lo == 1:
                if nums[mid] < nums[mid + 1]:return mid + 1
                else: return mid
            else:
                if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]: return mid
                elif nums[mid - 1] < nums[mid]: lo = mid
                elif nums[mid] > nums[mid + 1]: hi = mid
                else: lo = mid 
        
        return hi
​

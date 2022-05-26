class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        return self.sol2(nums)
​
    def sol1(nums):
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
    
    def sol2(self, nums):
        
        # 归到一个单调区间上，然后再做
        
        lo, hi = 0, len(nums) - 1
        
        while lo < hi:
            
            mid = (hi + lo) // 2
​
#             if mid > 0 and nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
#                 return mid
            
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        
        return lo

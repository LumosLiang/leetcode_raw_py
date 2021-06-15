# binary search
​
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        def bisearch(nums, lo, hi):
            if lo == hi: 
                if not nums[lo]: return '0'
                return nums[lo]
        
            if hi - lo == 1: return None
        
            mid = lo + (hi - lo) // 2
​
            if nums[mid] == nums[mid - 1]:
                return bisearch(nums, lo, mid) or bisearch(nums, mid + 1, hi)
​
            elif nums[mid] == nums[mid + 1]:
                return bisearch(nums, lo, mid - 1) or bisearch(nums, mid, hi)
​
            else: return nums[mid]
            
        return bisearch(nums, 0, len(nums) - 1)
        
   
            

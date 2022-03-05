class Solution:
    # O(logN), O(1)
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)
        
        while l < r:
            mid = (l + r) // 2
            val = nums[mid]
            
            if val < target:
                l = mid + 1
            else:
                r = mid
        
        return l 
            

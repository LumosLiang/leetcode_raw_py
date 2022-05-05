class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        
        # 还是划分到自己的区间内，
        # 斜率比较，还是要观察这种insight
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        
        return l
            

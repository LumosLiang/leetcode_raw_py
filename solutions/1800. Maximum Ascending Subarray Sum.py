class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        res = 0
        l, r = 0,0 
        
        while r < len(nums) - 1:
            if nums[r] >= nums[r + 1]:
                res = max(res, sum(nums[l:r + 1]))
                l = r + 1
            r += 1
        
        return max(res, sum(nums[l:r + 1]))

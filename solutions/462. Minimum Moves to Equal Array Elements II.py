class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        nums.sort()
        
        res, l, s = float('inf'), len(nums), sum(nums)
        pre_fix_sum = [None] * l
        
        for i in range(l):
            if i == 0:
                pre_fix_sum[i] = nums[i]
            else:
                pre_fix_sum[i] = pre_fix_sum[i - 1] + nums[i]
        
        for i in range(l):
            
            res = min(res, s - 2 * pre_fix_sum[i] + (2 * i + 2 - l) * nums[i])
            
        return res

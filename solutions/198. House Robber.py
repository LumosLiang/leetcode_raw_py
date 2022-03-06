class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # O(N), O(1)
        
        # dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        if len(nums) == 1: return nums[0]
        
        curr, pre_1, pre_2 = 0, max(nums[1], nums[0]), nums[0]
        
        for i in range(2, len(nums)):
            curr = max(nums[i] + pre_2, pre_1)
            pre_2 = pre_1
            pre_1 = curr
            
        return curr if curr != 0 else pre_1

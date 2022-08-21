class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        # 1 2 3 6
        
        # state -> nums[:i + 1] Largest Divisible Subset
        # function -> if nums[i] % nums[i - 1] or 
        # base
        
        nums.sort()
        
        dp = [[]] * len(nums)
        dp[0] = [nums[0]]
        
        for i in range(1, len(nums)):
            dp[i] = [nums[i]]
            for j in range(i):
                if 0 in [nums[i] % dp[j][-1], dp[j][-1] % nums[i]] and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        
        
        l, ans = 0, []
        
        for state in dp:
            if len(state) > l:
                ans = state
                l = len(state)
        
        return ans
            
            
        
        

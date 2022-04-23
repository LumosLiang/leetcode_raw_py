class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # 这是一个什么问题？
        
        # DFS 问题: 每一个状态都有选择，穷举的想法是，穷举所有的组合，选择递增的，在这个过程找最大的递增序列。
        # 一旦开始写memo，就进入了top-down DP的想法。
        
        memo = {}
        def DFS(nums, idx):
            
            if idx == len(nums) - 1:
                return 1
            
            if idx not in memo:
                memo[idx] = 1
                for i in range(idx + 1, len(nums)):
                    if nums[i] > nums[idx]:
                        memo[idx] = max(memo[idx], DFS(nums, i) + 1)
                
            return memo[idx]
        
        res = [DFS(nums, i) for i in range(len(nums))]
        return max(res)
    
    def DP(self, nums):  
        # DFS -> DP 问题，
        # state: 对于DFS，dp[i + 1] 是 nums[i + 1:]的最长的递增序列是多少。
        # dp[i] for j in i + 1 ~ len(nums) - 1, 如果nums[i] < nums[j], dp[i] = 1 + dp[j] 取最大的dp[i]
        # base： dp[0] = 1
        
        # O(N * N), O(N)
    
        dp = [1] * len(nums)
        
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    
    
            
        
        
        

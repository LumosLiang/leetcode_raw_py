class Solution:
    def canPartition(self, nums: List[int]) -> bool:
​
        return self.sol2(nums)
        
    # 错的，因为只有找一半就够了
    def sol1(self, nums):
        
        memo = {}
        def dfs(idx, ex_sum):
            nonlocal memo
​
            if idx == len(nums):
                return 1 if not ex_sum else 0
            
            if (idx, ex_sum) not in memo: 
                temp = dfs(idx + 1, ex_sum - nums[idx]) or dfs(idx + 1, ex_sum + nums[idx])
                memo[(idx, ex_sum)] = temp
        
            return memo[(idx, ex_sum)]
        
        return dfs(0, 0)
    
    # DP
    # 这个包里面正好 能够放入的物品的价值是 “一半”
    def sol2(self, nums):
​
        s, l = sum(nums), len(nums)
        t = s // 2
        if t != s / 2: return False
        
        dp = [[0 for i in range(t + 1)] for j in range(l)]
        
        # for i in range(l): dp[i][0] = 0
        
        for i in range(1, t + 1):
            if nums[0] < i:
                dp[0][i] = nums[0]
        
        for i in range(1, l):
            for j in range(1, t + 1):
                if nums[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
        
        return dp[l - 1][t] == t
        
        

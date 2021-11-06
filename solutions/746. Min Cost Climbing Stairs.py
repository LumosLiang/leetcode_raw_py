class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        l = len(cost)
        dp = [0] * (l + 1)
        
        for i in range(l + 1):
            if i < 2: dp[i] = cost[i]
            if i < l: dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
            else: dp[i] = min(dp[i - 1], dp[i - 2])
                
        return dp[l]

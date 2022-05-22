class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # DP 答案要什么，我的状态就是什么
        
        # i - 1  hold, sell, cooldown, 
        
        # i      hold, sell, cooldown, 
        
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        
        dp[0][0], dp[0][1], dp[0][2] = -prices[0], 0, 0
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i], -prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
        
        return max(dp[-1])
        
        

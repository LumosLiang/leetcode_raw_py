class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        
    
    def greedy():
        res = 0
        
        for i in range(1, len(prices)):
            curr, pre = prices[i], prices[i - 1]
            if curr > pre:
                res += curr - pre
        
        return res
    
    def dp()
    
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0], dp[0][1] = -prices[0], 0
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i], dp[i][0] + prices[i])
        
        return max(dp[-1])
    
    

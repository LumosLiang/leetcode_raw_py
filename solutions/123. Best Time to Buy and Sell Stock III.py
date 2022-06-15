class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 时间序列
        
        # DP maxprofit at different choice
        
        # i - 1  持有第一股， 卖出第一股， 持有第二股，卖出第二股
        
        # i      持有第一股， 卖出第一股， 持有第二股，卖出第二股
       
        dp = [[0 for _ in range(4)] for _ in range(len(prices))]
        
        # 设置初始值是一个难点
        dp[0][0], dp[0][1], dp[0][2], dp[0][3] = -prices[0], 0, -prices[0], 0
    
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])
            
            dp[i][2] = max(dp[i - 1][1] - prices[i], dp[i - 1][2])
            dp[i][3] = max(dp[i - 1][2] + prices[i], dp[i - 1][3])
        
        print(dp)
        return max(dp[-1])

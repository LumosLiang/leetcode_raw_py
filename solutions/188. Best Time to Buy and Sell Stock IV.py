class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
​
        # i - 1  持有第一股， 卖出第一股， 持有第二股，卖出第二股 .... 持有第 k 股， 卖出第 k 股，
        
        # i      持有第一股， 卖出第一股， 持有第二股，卖出第二股 .... 持有第 k 股， 卖出第 k 股，
        
        if not k or not prices: return 0
 
        dp = [[0 for i in range(k * 2)] for j in range(len(prices))]
        
        for i in range(2 * k):
            if not i % 2:
                dp[0][i] = -prices[0]
            else:
                dp[0][i] = 0
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], 0 - prices[i])
            for j in range(1, 2 * k):
                if not j % 2:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
​
        return max(dp[-1])

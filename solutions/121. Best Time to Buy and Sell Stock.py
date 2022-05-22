class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # DP 答案要什么，我在i点的状态就是什么
        
        # i - 1  持有 卖出
        # i      持有 卖出
        
        return self.sol3(prices)
        
    # 二维
    def sol1(self, prices):
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0], dp[0][1] = -prices[0], 0
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
        
        res = float('-inf')
        for state in dp:
            res = max(res, state[-1])
        
        return res if res > 0 else 0
    
    # 一维
    def sol2(self, prices):
        dp = [0] * len(prices)
        min_hold = prices[0]
        
        for i in range(1, len(prices)):
            min_hold = min(min_hold, prices[i])
            dp[i] = prices[i] - min_hold
        
        return max(dp)
        
    # O(1)
    def sol3(self, prices):
        
        min_hold = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            min_hold = min(min_hold, prices[i])
            max_profit = max(max_profit, prices[i] - min_hold)
        
        return max_profit

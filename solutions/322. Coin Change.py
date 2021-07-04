class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0, -1:float('inf')}
        
        def dp(i):
            if i not in memo:
                res = float('inf')
                for coin in coins:
                    subproblem = dp(i - coin)
                    res = min(res, 1 + subproblem)
                memo[i] = res if res != float('inf') else -1
            return memo[i]
        
        
        
        
        return dp(amount)
​

class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = (n + 1) * [0]
        dp[0] = 0
        
        for i in range(1, n + 1):
            temp_min = float('inf')
            maxps = math.floor(math.sqrt(i))
            
            for j in range(1, maxps + 1):
                temp_min = min(temp_min, dp[i - j ** 2])
            
            dp[i] = 1 + temp_min
            
        
        return dp[n]

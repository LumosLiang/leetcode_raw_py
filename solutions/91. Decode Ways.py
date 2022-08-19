class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        # how many ways for s[i:]
        @lru_cache(None)
        def dfs(i):
            
            if i == len(s): return 1
            
            if s[i] == "0": return 0
            
            temp = 0
            for j in range(1, 3):
                
                if i + j <= len(s) and 1 <= int(s[i:i + j]) <= 26:
                    
                    temp += dfs(i + j)
            
            return temp 
        
        return dfs(0)
    
​
    def DP(self, s):
        l = len(s)
        dp = [0] * (l + 1)
        dp[-1] = 1
        
        for i in range(l - 1, -1, -1):
            if s[i] == "0": continue
                            
            dp[i] = dp[i + 1]
​
            if i < l - 1:
​
                if s[i + 1] == 0 and s[i] < 3: 
                    dp[i] = dp[i + 2]
​
                elif s[i:i + 2] <= "26":
                    dp[i] += dp[i + 2]
        
        return dp[0]
        

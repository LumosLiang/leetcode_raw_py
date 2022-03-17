class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dp(s, p)
        
    def sol1(self, s, p):
        ls, lp = len(s), len(p)
        
        @lru_cache(None)
        
        def backtrack(i, j):
            
            if j == lp:
                return i == ls
            
            if j < lp and p[j] == "*":
                temp1 = backtrack(i, j + 1) # match empty string
                if i < ls: 
                    return (temp1 or backtrack(i + 1, j))
                return temp1
            
            if i < ls and (s[i] == p[j] or p[j] == "?"):
                return backtrack(i + 1, j + 1)
                
            return False    
                
        return backtrack(0, 0)
    
    
    def dp(self, s, p):
        ls, lp = len(s), len(p)
        
        dp = [[False for i in range(lp + 1)] for j in range(ls + 1)]
        dp[ls][lp] = True
        
        for i in range(ls, -1, -1):
            for j in range(lp, -1, -1):
                
                if j == lp and i != ls: dp[i][j] = False
                
                elif j < lp and p[j] == "*":
                    dp[i][j] = dp[i][j + 1] # match empty string
                    
                    if i < ls: 
                        dp[i][j] = dp[i][j] or dp[i + 1][j]
            
                elif i < ls and (s[i] == p[j] or p[j] == "?"):
                    dp[i][j] = dp[i + 1][j + 1]
                        
        return dp[0][0]

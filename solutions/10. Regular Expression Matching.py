class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.DP(s, p)
    # DFS
    # backforward
    def sol1(self, s: str, p: str):
        
        def DFS(i, j):
            
            if j == len(p):
                return i == len(s)
            
            if j < len(p) - 1 and p[j + 1] == "*":
                c1 = DFS(i, j + 2)
                c2 = DFS(i + 1, j)
                return c1 or c2
            
            if i < len(s) and (p[j] == '.' or p[j] == s[i]):
                return DFS(i + 1, j + 1)
                
        return DFS(0, 0)
        
        
    def DP(self, s: str, p: str):
        
        ls, lp = len(s), len(p)
        
        dp = [[False for i in range(lp + 1)] for j in range(ls + 1)]
        
        dp[ls][lp] = True
        
        for i in range(ls, -1, -1):
            for j in range(lp, -1, -1):
                if j == lp and i != ls: 
                    dp[i][j] = False
                    
                elif j + 1 < lp and p[j + 1] == '*':
                    temp = dp[i][j + 2]
                    if i < len(s) and (p[j] == "." or p[j] == s[i]):
                        dp[i][j] = temp or dp[i + 1][j]
                    else: 
                        dp[i][j] = temp
                
                elif i < ls and (p[j] == '.' or p[j] == s[i]):
                    dp[i][j] = dp[i + 1][j + 1]
                    
        return dp[0][0]
​
        
        
        
        
        
        

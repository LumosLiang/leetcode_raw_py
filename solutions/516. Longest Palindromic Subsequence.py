class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        return self.DP(s)
    
    def DFS(self, s):
        
        # return s[i:j] 最长的LPS
        # "bbbbab"
    
        @lru_cache(None)
        def backtrack(i, j):
            if j < i: return 0
            
            if i == j: return 1
            
            if s[i] == s[j]:
                # defintely can fit the known LPS
                return 2 + backtrack(i + 1, j - 1)
            else:
                return max(backtrack(i, j - 1), backtrack(i + 1, j))
            
        return backtrack(0, len(s) - 1)
    
    def DP(self, s):
        
        l = len(s)
        dp = [[0 for i in range(l)] for j in range(l)]
        
        for i in range(l):
            for j in range(l):
                if i == j: dp[i][j] = 1
                if i > j: dp[i][j] = 0
                    
        for j in range(1, l):
            for i in range(l - j):
                if s[i] == s[i + j]:
                    dp[i][i + j] = 2 + dp[i + 1][i + j - 1]
                else:
                    dp[i][i + j] = max(dp[i][i + j - 1], dp[i + 1][i + j])
        
        return dp[0][l - 1]
        
    

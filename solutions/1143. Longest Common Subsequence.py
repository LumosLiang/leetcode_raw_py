class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.DP(text1, text2)
    
    def DP(self, text1: str, text2: str):
        
        # dp[i][j] -> text1[i:] 和 text2[j:] 的 LCS
        
        m, n = len(text1), len(text2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]
        
    def backtrack(self, text1: str, text2: str):
        
        m, n = len(text1), len(text2)
        
        # text1[i:] 和 text2[j:] 的 LCS
        
        @lru_cache(None)
        def dfs(i, j):
            if i == m: return 0
            if j == n: return 0
           
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            
            if text1[i] != text2[j]:
                return max(dfs(i, j + 1), dfs(i + 1, j))
                
        return dfs(0, 0)

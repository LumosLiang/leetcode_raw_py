class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        return self.DP2(word1, word2)
    
    # The reverse of LCS
    def DP1(self, text1: str, text2: str):
        # dp[i][j] -> text1[i:] 和 text2[j:] 的 LCS
        
        m, n = len(text1), len(text2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return m + n - 2 * dp[0][0]
​
    def DFS(self, word1: str, word2: str):
        
        l1, l2 = len(word1), len(word2)
        
        # word1[i:] 和 word2[j:] 的 minimum steps to make them the same
        @lru_cache(None)
        def backtrack(i, j):
            
            if i == l1: return l2 - j
            if j == l2: return l1 - i
            
            if word1[i] == word2[j]:
                return backtrack(i + 1, j + 1)
            else:
                return 1 + min(backtrack(i, j + 1), backtrack(i + 1, j))
                
        return backtrack(0, 0)
    
    
    def DP2(self, text1: str, text2: str):
        
        m, n = len(text1), len(text2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        
        for i in range(m): dp[i][n] = m - i 
        for j in range(n): dp[m][j] = n - j 
                
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        return self.DP(s1, s2)
        
    def DFS(self, s1: str, s2: str):
        
        l1, l2 = len(s1), len(s2)
        
        # word1[i:] 和 word2[j:] 的 minimum ASCII Delete Sum to make them the same
        
        @lru_cache(None)
        def backtrack(i, j):
            if i == l1: return sum([ord(s2[x]) for x in range(j, l2)])
            if j == l2: return sum([ord(s1[y]) for y in range(i, l1)])
            
            if s1[i] == s2[j]:
                return backtrack(i + 1, j + 1)
            else:
                return min(ord(s2[j]) + backtrack(i, j + 1), ord(s1[i]) + backtrack(i + 1, j))
                
        return backtrack(0, 0)
    
    
    def DP(self, s1: str, s2: str):
        
        m, n = len(s1), len(s2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        
        for i in range(m): dp[i][n] = sum([ord(s1[y]) for y in range(i, m)])
        for j in range(n): dp[m][j] = sum([ord(s2[y]) for y in range(j, n)])
                
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(ord(s2[j]) + dp[i][j + 1], ord(s1[i]) + dp[i + 1][j])
        
        return dp[0][0]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        l1, l2 = len(word1), len(word2)
        
        @lru_cache(None)
        def dfs(i, j):    
​
            if i == l1: return l2 - j
            if j == l2: return l1 - i
​
            if word1[i] == word2[j]: return dfs(i + 1, j + 1)
​
            if word1[i] != word2[j]: return 1 + min(dfs(i + 1, j), dfs(i + 1, j + 1), dfs(i, j + 1))
            
        return dfs(0, 0)

class Solution:
    def minInsertions(self, s: str) -> int:
        
        @lru_cache(None)
        def dfs(i, j):
            if i >= j: return 0
            
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            else:
                return 1 + min(dfs(i, j - 1), dfs(i + 1, j))
            
            
        return dfs(0, len(s) - 1)
    

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        l1, l2 = len(s), len(t)
        
        @lru_cache(None)
        def dfs(i, j):
            
            if j == l2: return 1
            
            if i < l1 and j < l2:
                if s[i] == t[j]:
                
                    return dfs(i + 1, j + 1) + dfs(i + 1, j)
            
                else:
                
                    return dfs(i + 1, j)
            
            return 0
            
        return dfs(0, 0)

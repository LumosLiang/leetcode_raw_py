class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        l1, l2, l3 = len(s1), len(s2), len(s3)
        
        # s1[i:], s2[j:] -> s3[i + j:]
        
        # @lru_cache(None)
        
        memo = {(l1, l2): l1 + l2 == l3}
        
        def dfs(i, j):
            
            if i == l1 and j == l2 and i + j == l3: return True 
            
            if (i, j) not in memo:
                memo[(i,j)] = False
                if i + j < l3:
                    if i < l1 and j < l2 and s1[i] == s2[j] and s3[i + j] == s1[i]:
                        memo[(i, j)] = dfs(i + 1, j) or dfs(i, j + 1)    
​
                    elif i < l1 and s3[i + j] == s1[i]:
                        memo[(i, j)] = dfs(i + 1, j)
​
                    elif j < l2 and s3[i + j] == s2[j]:
                        memo[(i, j)] = dfs(i, j + 1)
                
            return memo[(i, j)]
        
        dfs(0, 0)
        return memo[(0, 0)]
    
    

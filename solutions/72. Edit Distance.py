class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        return self.DFS(word1, word2)
    
    def DFS(self, word1: str, word2: str):
        
        # minimum number of operations required to convert word1[i:] to word2[j:] 
        l1, l2 = len(word1), len(word2)
        
        @lru_cache(None)
        def backtrack(i, j):
            
            # insert
            if i == l1: return l2 - j
            # delete
            if j == l2: return l1 - i
            
            # ros -> ro
            if word1[i] == word2[j]:
                return backtrack(i + 1, j + 1)
            else:
                # aros -> dro       delete                  replace              insert
                return 1 + min(backtrack(i, j + 1), backtrack(i + 1, j + 1), backtrack(i + 1, j))
        
        return backtrack(0, 0)
​
       

class Solution:
    # O(C(n, k))
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(choices, path):
            if len(path) == k:
                res.append(path[:])
                return
        
            for i in range(len(choices)):
                backtrack(choices[i+1:], path + [choices[i]])
        
        backtrack(range(1, n + 1), [])
        return res
    
    # optimal way should be with start

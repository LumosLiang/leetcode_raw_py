class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        res = []
        d = {"a":["b", "c"], "b":["a", "c"], "c":["a", "b"]}
        
        def backtrack(choices, path):
            if len(path) == n:
                res.append(path)
                return
            
            for c in choices:
                backtrack(d[c], path + c)
        
        backtrack(['a', 'b', 'c'], '')
        return res[k - 1] if k <= len(res) else ""

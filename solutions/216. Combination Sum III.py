class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def helper(choices, path, start, s, l):
            if l == k and s == 0:
                res.append(path)
                return
                
            for i in range(start, len(choices)):
                helper(choices, path + [choices[i]], i + 1, s - choices[i], l + 1)        
        
        helper([i for i in range(1,10)], [], 0, n, 0)
        return res

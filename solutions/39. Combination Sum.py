class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(choices, path, s):
            if s == 0:
                res.append(path)
                return
            elif s < 0:
                return
            
            for i in range(len(choices)):
                helper(choices[i:], path + [choices[i]], s - choices[i])
            
        helper(candidates, [], target)
        return res
        

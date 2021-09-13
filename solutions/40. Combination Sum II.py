class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def helper(choices, path, s):
            if s == 0:
                res.append(path)
                return
            elif s < 0:
                return
            
            for i in range(len(choices)):
                if i > 0 and choices[i] == choices[i - 1]: continue
                helper(choices[i + 1:], path + [choices[i]], s - choices[i])
            
        helper(candidates, [], target)
        return res
        

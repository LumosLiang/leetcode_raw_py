# Trik is excluding duplicate zat 
# choices[i:]
​
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(choices, start, path, s):
            if s == 0:
                res.append(path)
                return
            elif s < 0:
                return
            
            for i in range(start, len(choices)):
                helper(choices, i, path + [choices[i]], s - choices[i])
            
        helper(candidates, 0, [], target)
        return res
        
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(choices, path):
            if sum(path) == target:
                res.append(path)
                return
            elif sum(path) > target:
                return
            
            for i in range(len(choices)):
                helper(choices[i:], path + [choices[i]])
            
        helper(candidates, [])
        return res
        

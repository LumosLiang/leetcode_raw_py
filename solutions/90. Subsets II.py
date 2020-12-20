class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
​
        def backtrack(choices, path):
            res.append(path)
            
            for i in range(len(choices)):
                if i > 0 and choices[i] == choices[i - 1]:
                    continue
                backtrack(choices[i + 1:], path + [choices[i]])
            
        backtrack(sorted(nums), [])
        
        return res

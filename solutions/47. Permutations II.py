class Solution:
    
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        
        def backtrack(choices, track):
            if not choices:
                res.append(track)
            
            for i in range(len(choices)):
                if i > 0 and choices[i] == choices[i-1]:
                    continue
                backtrack(choices[:i] + choices[i+1:], track + [choices[i]])
            
            
        backtrack(nums, [])
        
        return res
​

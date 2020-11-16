class Solution:
    
    def permute(self, nums):
        res = []
        
        def backtrack(choices, track):
            if not choices:
                res.append(track[:])
                
            for i in range(len(choices)):
                backtrack(choices[:i] + choices[i+1:], track + [choices[i]])
                
        backtrack(nums, [])
        
        return res
   
    

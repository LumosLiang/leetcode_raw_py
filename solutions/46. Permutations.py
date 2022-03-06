class Solution:
    # O(N*N!), O(N!)
    def permute(self, nums):
        res = []
        
        def backtrack(choices, track):
            if not choices:
                res.append(track)
                return
                
            for i in range(len(choices)):
                backtrack(choices[:i] + choices[i+1:], track + [choices[i]])
                
        backtrack(nums, [])
        
        return res
   
    

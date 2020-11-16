class Solution:
    def combine(self, n, k):
        res = []
        
        def backtrack(choices, count, track):
            if len(track) == count:
                res.append(track[:])
                return
            
            for i in range(len(choices)):
                backtrack(choices[i+1:], count, track + [choices[i]])
​
        backtrack(range(1,n+1), k, [])
        
        return res
​
               
                

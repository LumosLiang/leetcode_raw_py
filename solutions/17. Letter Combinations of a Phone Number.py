dt = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits is "":return []
        
        res = []
        
        def backtrack(choices, path, l):
            if len(path) == l:
                res.append(path)
                return
            
            for i in range(len(choices)):
                temp = dt[choices[i]]
                for j in range(len(temp)):
                    backtrack(choices[i+1:], path + temp[j], l)
                
        backtrack(digits, '', len(digits))
        return res
                
            
        
        

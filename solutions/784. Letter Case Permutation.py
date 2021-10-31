class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = []
        
        def backtrack(lst, path, idx):
            
            if(len(path) ==  len(lst)): 
                res.append(''.join(path))
            else:
                c = lst[idx]
                if str.isalpha(c):
                    backtrack(lst, path + [c.lower()], idx + 1)
                    backtrack(lst, path + [c.upper()], idx + 1)
                else:
                    backtrack(lst, path + [c], idx + 1)
            
        backtrack(list(s), [], 0)    
        
        return res
        
        
        
        
        

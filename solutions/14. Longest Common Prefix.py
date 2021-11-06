class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1: return strs[0]
        
        res, p = "", 0
        
        while (self.isequal(strs, p)):
            res += strs[0][p]
            p += 1
        
        return res
    
    def isequal(self, strs, p):
        
        res = True
        
        for i in range(len(strs) - 1):
            if strs[i][p:] and strs[i + 1][p:] and strs[i][p] == strs[i + 1][p]: continue
            else: return False
            
        return res

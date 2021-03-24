class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dit = {}
        
        for i in s:
            if i in dit:
                dit[i] += 1
            else:
                dit[i] = 1
        
        for j in t:
            if j not in dit:
                return False
            else:
                dit[j] -= 1
        
        for k, v in dit.items():
            if v != 0:
                return False
        
        return True

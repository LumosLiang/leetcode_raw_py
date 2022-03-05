class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        r, m = collections.Counter(ransomNote), collections.Counter(magazine)
        
        for k, v in r.items():
            if k not in m or m[k] < v:
                return False
            
        return True

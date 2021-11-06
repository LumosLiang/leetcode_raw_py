class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        rn_hash, maga_hash = collections.Counter(list(ransomNote)), collections.Counter(list(magazine))
        
        count = 0
        for key, value in rn_hash.items():
            if key in maga_hash and maga_hash[key] >= value:count+=1
        
        return count == len(rn_hash)
                

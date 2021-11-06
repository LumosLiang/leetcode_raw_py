class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hash = {}
        
        for i in range(len(s)):
            if s[i] in hash: hash[s[i]][0] += 1
            else: hash[s[i]] = [1, i]
        
        for value in list(hash.values()):
            if value[0] == 1: return value[1]
        
        return -1

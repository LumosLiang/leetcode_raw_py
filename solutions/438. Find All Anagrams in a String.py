class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        
        # need: p's anagram
        # window: length is the same and frequecy is the same.
        # where to update, as long as we find the one
        
        
        res = []
        window, need = collections.Counter(), collections.Counter(p)
        l, length, count = 0, len(p), 0
        
        for r, val in enumerate(s):
            window[val] += 1
            if val in need and window[val] == need[val]:
                count += 1
                
            if r - l + 1 == length:
                if count == len(need): 
                    res.append(l)
                
                if s[l] in need and window[s[l]] == need[s[l]]:
                    count -= 1
                window[s[l]] -= 1
                l += 1
                    
        return res
        
 
        

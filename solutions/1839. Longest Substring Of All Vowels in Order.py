zclass Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
​
        l = 0
        seen = set()
        res = 0
        
        for r, v in enumerate(word):
            if r > 0 and v < word[r - 1]:
                l = r
                seen = set()
            seen.add(v)
            if len(seen) == 5:
                res = max(res, r - l + 1)
                
        return res
                
            
        
        
        

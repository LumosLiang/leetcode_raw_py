class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res, l = 0, 0
        window = {}
        
        # sliding window
        # construct window: no repeat characters.
        # criteria, need 
        # when to update.
        # improvement: like state compressing
        
        for r, val in enumerate(s):
            
            if val in window and l <= window[val]:
                l = window[val] + 1
                
            window[val] = r
            res = max(res, r - l + 1)
            
        return res

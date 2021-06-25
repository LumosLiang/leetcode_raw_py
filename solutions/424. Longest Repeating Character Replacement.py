class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        res = 0
        window = collections.Counter()
        
        for end in range(len(s)):
            window[s[end]] += 1
            while end - start + 1 - max(window.values()) > k:
                window[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
            
        return res
        
        

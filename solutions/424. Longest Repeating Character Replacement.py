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
        
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
    # 本质，我已经有的长度 - 最多的element <= k
        
        start = 0
        res = 0
        maxf = 0
        
        window = collections.Counter()
        
        for end, val in enumerate(s):
            window[val] += 1
            maxf = max(maxf, window[val])
            while end - start + 1 - maxf > k:
                window[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
            
        return res

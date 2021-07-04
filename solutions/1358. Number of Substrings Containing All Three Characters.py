class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start = 0
        res = 0
        window = collections.Counter()
        
        for end, val in enumerate(s):
            window[val] += 1
            while len(window) == 3:
                res += len(s) - end
                window[s[start]] -= 1
                if not window[s[start]]: del window[s[start]]
                start += 1
                
        return res

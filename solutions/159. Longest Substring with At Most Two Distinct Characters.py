class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        # longest
        # At Most Two Distinct Characters
        
        # sliding window
        # window -> dict
        
        window = collections.defaultdict(int)
        l = 0
        res = 0

        for r, val in enumerate(s):
            window[val] += 1
            
            while len(window) == 3:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            
            res = max(res, r - l + 1)

        return res

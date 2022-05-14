class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        # sliding window.
        # sliding window 还是不行。
        # 加constraint。atmost的方法？
        # all occurrence - less than one occurrence of all these characters a, b and c
        
        # "abcabc"
        # 1 + 2 + 3 + 4 + 5 + 6
        # 1 + 2 + 2 + 2 + 2 + 2
        
        def helper(s):
            l = 0
            res = 0
            window = collections.Counter()
            
            for r, val in enumerate(s):
                window[val] += 1
                while len(window) == 3:
                    window[s[l]] -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]
                    l += 1
                res += r - l + 1
        
            return res
        
        return sum(range(1, len(s) + 1)) - helper(s)
        
    # a better way
    # once you satisfy, the rest of the length are all qualfied answer
    
    def numberOfSubstrings2(self, s: str) -> int:
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

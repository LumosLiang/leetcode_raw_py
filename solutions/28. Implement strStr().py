class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack): return -1
        
        p1, p2 = 0, 0
        start = False
        res = 0
        
        while p1 < len(haystack) and p2 < len(needle):
            if not start:
                if haystack[p1] != needle[p2]: p1 += 1
                else:
                    start = True
                    res = p1
                    p1 += 1
                    p2 += 1
            else:
                if haystack[p1] == needle[p2]: 
                    p1 += 1
                    p2 += 1
                else:
                    start = False
                    res = 0
                    p1 = p1 - p2 + 1
                    p2 = 0
        
        return -1 if p2 <= len(needle) - 1 else res
                

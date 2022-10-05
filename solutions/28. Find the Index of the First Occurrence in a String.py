class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        "aabaabaaf"
        "aabaaf"
        
        def getTable(needle):
            
            table = [0] * len(needle)
            l = 0
            
            for r in range(1, len(needle)):
                while l > 0 and needle[l] != needle[r]:
                    l = table[l - 1]
                if needle[l] == needle[r]:
                    l += 1
                    table[r] = l
            
            return table
            
        table = getTable(needle)
        p1 = 0
        
        for p2, val in enumerate(haystack):
            
            while p1 > 0 and val != needle[p1]:
                p1 = table[p1 - 1]
            if val == needle[p1]:
                p1 += 1
            if p1 == len(needle):
                return p2 - len(needle) + 1
                
        return -1
            
        

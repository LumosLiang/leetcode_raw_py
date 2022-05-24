class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        return self.sol2(version1, version2)
    
    def sol1(self, version1: str, version2: str):
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        p1, p2 = 0, 0
       
        while p1 < len(v1) and p2 < len(v2):
            val1, val2 = int(v1[p1]), int(v2[p2])
            if val1 > val2: return 1
            if val1 < val2: return -1
            p1 += 1
            p2 += 1
            
        if p1 == len(v1) and sum([int(item) for item in v2[p2:]]): return -1
        if p2 == len(v2) and sum([int(item) for item in v1[p1:]]): return 1
    
        return 0
        
​
    def sol2(self, version1: str, version2: str):
        def split(s):
            res = []
            l = 0
            for r in range(len(s) + 1):
                if r == len(s) or s[r] == ".":
                    res.append(s[l:r])
                    l = r + 1
​
            return res
        
#         def remove_zero(s):
#             p = 0
#             if len(s) <= 1: return s
            
#             while p < len(s) and s[p] == "0": p += 1
​
#             if p == len(s): return "0"
#             else: return s[p:]
​
        v1, v2 = split(version1), split(version2)
       
        p1, p2 = 0, 0
        while p1 < len(v1) and p2 < len(v2):
            val1, val2 = int(v1[p1]), int(v2[p2])
            if val1 > val2: return 1
            if val1 < val2: return -1
            p1 += 1
            p2 += 1
            
        if p1 == len(v1) and sum([int(item) for item in v2[p2:]]): return -1
        if p2 == len(v2) and sum([int(item) for item in v1[p1:]]): return 1
    
        return 0
    

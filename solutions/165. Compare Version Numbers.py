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

    def sol2(self, version1: str, version2: str):
        def split(s):
            res = []
            l = 0
            for r in range(len(s) + 1):
                if r == len(s) or s[r] == ".":
                    res.append(s[l:r])
                    l = r + 1

            return res
        
#         def remove_zero(s):
#             p = 0
#             if len(s) <= 1: return s
            
#             while p < len(s) and s[p] == "0": p += 1

#             if p == len(s): return "0"
#             else: return s[p:]

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
    

    def sol3(self, version1: str, version2: str) -> int:
         
        def helper(string, p):
            l, r = p, p
            
            while r < len(string):
                
                while r < len(string) and string[r] != ".":
                    r += 1

                if int(string[l:r]) != 0:
                    return True
                r = r + 1
                l = r
                
            return False
            
        l1, r1, l2, r2 = 0, 0, 0, 0
        len1, len2 = len(version1), len(version2)
        
        while r1 < len1 and r2 < len2:
            
            while r1 < len1 and version1[r1] != ".": r1 += 1
            
            temp1 = int(version1[l1:r1])
            
            while r2 < len2 and version2[r2] != ".": r2 += 1

            temp2 = int(version2[l2:r2])
            
            if temp1 > temp2: return 1
            elif temp1 < temp2: return -1
            
            if r1 < len1:
                r1 = r1 + 1
                l1 = r1
            if r2 < len2:
                r2 = r2 + 1
                l2 = r2
        
        if r1 == len1 and helper(version2, r2): return -1
        
        if r2 == len2 and helper(version1, r1): return 1
        
        return 0
    
  

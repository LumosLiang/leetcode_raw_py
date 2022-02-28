class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        c1, c2 = collections.Counter(s), collections.Counter(t)
        
        r1, r2 = 0, 0
        
        for k, v in c1.items():
            if k in c2:
                r1 += abs(c2[k] - v)
            else:
                r1 += v
        
        for k, v in c2.items():
            if k not in c1:
                r2 += v
        
        return r1 + r2

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        c1, c2 = collections.Counter(s), collections.Counter(t)
        
        for k, v in c2.items():
            if k in c1:
                c1[k] = c1[k] - v if v <= c1[k] else 0
        
        return sum(c1.values())

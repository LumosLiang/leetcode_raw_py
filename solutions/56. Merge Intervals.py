class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Just simple simulation, draw this on the paper, and you will get it
        # O(NlogN)
        
        intervals.sort()
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            nxt = intervals[i]
            if nxt[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], nxt[1])
            else:
                res.append(nxt)
        
        return res
        
        
        

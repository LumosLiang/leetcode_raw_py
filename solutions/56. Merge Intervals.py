class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals: return None
​
        intervals.sort(key = lambda intv: intv[0])
        
        res = []
        res.append(intervals[0])
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= res[-1][1]:
                res[-1][1] = max(curr[1], res[-1][1])
            elif curr[0] > res[-1][1]:
                res.append(curr)
        
        return res
        
        
                
                

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda intv: intv[0])
        res = 0
        
        pre = intervals[0]
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] == pre[0] and curr[1] > pre[1]: pre, curr = curr, pre
​
            if curr[1] <= pre[1]: res += 1
            elif curr[0] < pre[1] < curr[1] or curr[0] >= pre[1]: pre = curr
                
        return len(intervals) - res
        
            
        

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    
    #    ---   ---- ----- ----- - --- --
    #        ---------------
    # --
    #        -
    #                --
​
    # if nI[end] < interval[0][0] or if nI[start] > interval[-1][1]
​
    # loop each interval, [left, right], 
    
    
        if not intervals: return [newInterval]
        res = []
        
        start, end = newInterval[0], newInterval[1]
        
        flag_set = False
        for i in range(len(intervals)):
            if flag_set:
                res.append(intervals[i])  
            else:
                if start > intervals[i][1]: 
                    res.append(intervals[i])
                else:
                    if end < intervals[i][0]:
                        res.append([start, end])
                        res.append(intervals[i])
                        flag_set = True
                    else:
                        start = min(start, intervals[i][0]) 
                        end = max(end, intervals[i][1])
        
        if not flag_set: return res + [[start, end]]
        return res
        
    
            

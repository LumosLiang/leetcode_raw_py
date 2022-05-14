class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # max min的概念
        # O(NlogN)
        
        
        intervals.sort()
        merge = [intervals[0]]
        for i in range(1, len(intervals)):
            nxt = intervals[i]
            if merge[-1][1] >= nxt[0]:
                merge[-1][1] = max(merge[-1][1], nxt[1])
            else:
                merge.append(nxt)
        return merge
        
        

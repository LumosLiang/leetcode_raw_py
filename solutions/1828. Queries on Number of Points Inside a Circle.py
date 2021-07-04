class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        
        res = []
        for q in queries:
            r = q.pop()
            count = 0
            for p in points:
                if ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5 <= r:
                    count += 1
            res.append(count)
        return res
                

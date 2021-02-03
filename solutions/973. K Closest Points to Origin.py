import heapq
class Solution:
    def kClosest(self, points, K):
        ans = []
        for p in points:
            heapq.heappush(ans, (-(p[0] ** 2 + p[1] ** 2), p))
            if len(ans) > K:    
                heapq.heappop(ans)
        
        return [a[1] for a in ans]

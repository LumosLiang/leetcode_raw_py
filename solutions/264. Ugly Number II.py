class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        if n == 1: return 1
        
        heap = []
        cnt = 0
        
        heapq.heappush(heap, 2)
        heapq.heappush(heap, 3)
        heapq.heappush(heap, 5)
        
        visited = {2,3,5}
        
        while cnt < n - 2:
            temp = heapq.heappop(heap)
            if temp * 2 not in visited:
                heapq.heappush(heap, temp * 2)
                visited.add(temp * 2)
            if temp * 3 not in visited:
                heapq.heappush(heap, temp * 3)
                visited.add(temp * 3)
            if temp * 5 not in visited:
                heapq.heappush(heap, temp * 5)
                visited.add(temp * 5)
            cnt += 1
            
        return heap[0]
        
        
        
        

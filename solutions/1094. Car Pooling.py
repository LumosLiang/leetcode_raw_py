class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # (2) 1 ---- 5
        #     (3) 3 ---- 7
        return self.sol2(trips, capacity)
    
    def sol1(self, trips, capacity):
        h = collections.defaultdict(int)
        
        for trip in trips:
            h[trip[1]] += trip[0] 
            h[trip[2]] -= trip[0]
        
        s = 0
        for location in sorted(h):
            s += h[location]
            if s > capacity:
                return False
        
        return True
        
    def sol2(self, trips, capacity):
        
        heap = []
        
        trips.sort(key = lambda x: x[1])
        
        heapq.heappush(heap, (trips[0][2], trips[0][1], trips[0][0]))
        people_cnt = trips[0][0]
        
        if people_cnt > capacity: return False
    
        for i in range(1, len(trips)):
            
            while heap and trips[i][1] >= heap[0][0]:
                end, start, num = heapq.heappop(heap)
                people_cnt -= num
                
            heapq.heappush(heap, (trips[i][2], trips[i][1], trips[i][0]))
            people_cnt += trips[i][0]
​
            if people_cnt > capacity:
                return False
         
        return True
        

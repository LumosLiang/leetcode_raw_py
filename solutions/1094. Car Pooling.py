class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # (2) 1 ---- 5
        #     (3) 3 ---- 7
        
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
        
            
        

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
#         sliding window + 2 * heap
        
#         8, 2
#         2, 4, 2, 7
#         4, 7
        
        
#         8, 8
#         2,8    2
#         2,4,8  4,2
#         2,2,4,8  4,2,2
#         7,8    7,4,2,2
        
        
        minheap, maxheap = [], []
        l = 0
        res = 0
        
        for r, val in enumerate(nums):
            heapq.heappush(minheap, (val, r))
            heapq.heappush(maxheap, (-val, r))
​
            while -maxheap[0][0] - minheap[0][0] > limit:
                l += 1
                
                while minheap and minheap[0][1] < l:
                    heapq.heappop(minheap)
                
                while maxheap and maxheap[0][1] < l:
                    heapq.heappop(maxheap)
            
            res = max(res, r - l + 1)
        
        return res
        
        
        
        

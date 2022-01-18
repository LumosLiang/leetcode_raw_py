class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        minheap = []
        
        for num in nums:
            heappush(minheap, int(num))
            if len(minheap) > k:
                heappop(minheap)
        
        return str(minheap[0])
​
        
        
        
        

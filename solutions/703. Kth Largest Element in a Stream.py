class KthLargest:
​
    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._heap = []
        for num in nums:
            self.add(num)
​
    def add(self, val: int) -> int:
        
        if len(self._heap) < self._k:
            heapq.heappush(self._heap, val)
        else:
            heapq.heappushpop(self._heap, val)
        return self._heap[0]
​
        
​
​
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
​

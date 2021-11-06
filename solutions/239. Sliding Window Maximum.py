class MonoQ:
    def __init__(self):
        self.data = collections.deque()
        
    def push(self, n):
        while self.data and self.data[-1] < n:
            self.data.pop()
        self.data.append(n)
        
    def getMax(self):
        return self.data[0]
        
    def pop(self, n):
        if self.data and self.data[0] == n:
            self.data.popleft()
​
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = MonoQ()
        res = []
        
        for i in range(len(nums)):
            if i < k - 1:
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.getMax())
                window.pop(nums[i - k + 1])
        return res

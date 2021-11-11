class MedianFinder:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
​
    def addNum(self, num: int) -> None:
        if len(self.large) == len(self.small):
            heappush(self.small, -num)
            heappush(self.large, -heappop(self.small))
        else:
            heappush(self.large, num)
            heappush(self.small, -heappop(self.large))
            
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        if len(self.large) - 1 == len(self.small):
            return self.large[0]

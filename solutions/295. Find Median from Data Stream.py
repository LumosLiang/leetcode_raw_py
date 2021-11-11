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
            heappush(self.large, -heappushpop(self.small,-num))
        else:
            heappush(self.small, -heappushpop(self.large,num))
            
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        if len(self.large) - 1 == len(self.small):
            return self.large[0]

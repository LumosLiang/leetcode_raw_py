class FrontMiddleBackQueue:
​
    def __init__(self):
        self._q1 = deque()
        self._q2 = deque()
​
    def pushFront(self, val: int) -> None:
        self._q1.appendleft(val)
        if len(self._q1) > len(self._q2) + 1:
            self._q2.appendleft(self._q1.pop())
​
    def pushMiddle(self, val: int) -> None:
        
        if len(self._q1) > len(self._q2):
            self._q2.appendleft(self._q1.pop())
        self._q1.append(val)
​
    def pushBack(self, val: int) -> None:
        
        self._q2.append(val)
        if len(self._q2) > len(self._q1):
            self._q1.append(self._q2.popleft())
​
    def popFront(self) -> int:
        if not self._q1: return -1 
        
        res = self._q1.popleft()
        if len(self._q2) > len(self._q1):
            self._q1.append(self._q2.popleft())
        return res
​
    def popMiddle(self) -> int:
        if not self._q1: return -1
        
        res = self._q1.pop()
        if len(self._q2) > len(self._q1):
            self._q1.append(self._q2.popleft())
        return res
        
    def popBack(self) -> int:
        
        # empty check
        if not self._q2 and not self._q1:return -1
        if not self._q2: return self._q1.pop()
        
        res = self._q2.pop()
        if len(self._q1) > len(self._q2) + 1:
            self._q2.appendleft(self._q1.pop())
        return res
        
​
​

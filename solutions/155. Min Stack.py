class MinStack:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
              
    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.getMin())))
​
    def pop(self) -> None:
        self.stack.pop()
​
    def top(self) -> int:
        return self.stack[-1][0]
​
    def getMin(self) -> int:
        if len(self.stack) == 0:
            return float('inf')
        else:
            return self.stack[-1][1]
​

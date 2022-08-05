from collections import deque

# if using deque, I should only use deque: append, and popleft

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        tempq = deque()
        tempq.append(x)
        tempq.append(self.q)
        self.q = tempq
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        res = self.q.popleft()
        self.q = self.q.popleft()
        return res
    
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


class MyStack1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        self._top = None
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        self._top = x
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1) > 1:
            self._top = self.q1.popleft()
            self.q2.append(self._top)
        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return result
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0

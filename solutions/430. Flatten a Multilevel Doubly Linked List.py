"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
# recursion
​
class Solution:
   
    def flatten(self, head: 'Node') -> 'Node':
        
        def helper(head):
        
            curr, p, s, t = head, None, None, None
​
            while curr:
                if curr.child:
                    p = curr
                    s = curr.next
                if not curr.next:
                    t = curr
                curr = curr.next
​
            if not p: return [head, t]
            
            start, end = helper(p.child)
            
            p.child = None
            p.next = start
            start.prev = p
            
            if s:
                end.next = s
                s.prev = end
                return [head, t]
            else: return [head, end]
                
        return helper(head)[0]

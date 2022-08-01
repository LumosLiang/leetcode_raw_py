"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
​
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
   
        return self.sol2(head)
        
    # O(N), O(N)
    def sol1(self, head):
        if not head: return None
   
        # 1. if want to deep_copy, then just loop, at every step, just continue create new ListNode
        # 2. but questions is how to link with the correct one on random and next field, instead of creating incorrect new              ones.
        # 3. use hash to store this match relationship
        
        # hash = [key:(next, random, new)]
​
        if not head: return None
    
        h = {}
        curr = head
        
        while curr:
            h[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next: h[curr].next = h[curr.next]
            else: h[curr].next = None
            
            if curr.random: h[curr].random = h[curr.random]
            else: h[curr].random = None
            
            curr = curr.next
        
        return h[head]
    
    # O(N), O(1)    
    def sol2(self, head):
        
        if not head: return None
        
        curr, nxt = head, None
        
        # directly "insert" the copied node 
        while curr:
            nxt = curr.next
            curr.next = Node(curr.val)
            curr.next.next = nxt
            curr = nxt
        
        

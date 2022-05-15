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
        h = {}
        curr = head
        
        while curr:
            h[curr] = [curr.next, curr.random, Node(curr.val)]
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next: h[curr][2].next = h[curr.next][2]
            else: h[curr][2].next = None
            if curr.random: h[curr][2].random = h[curr.random][2]
            else: h[curr][2].random = None
            curr = curr.next
        
        return h[head][2]
            
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
        
        
        # link random
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # split each other, refer: odd/even linked list
        # 7 -> 7' -> 13 -> 13' -> 11 -> 11' -> 10 -> 10' -> 1 -> 1'
        
        new_head = head.next
        curr, curr_new = head, head.next
        
        while curr_new.next:
            curr.next = curr.next.next
            curr_new.next = curr_new.next.next
            curr = curr.next
            curr_new = curr_new.next
        
        return new_head
        

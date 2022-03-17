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
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        # hash table
        
        # loop each node, generate its clone. and put the pair in the hash table
        # loop each node, use its clone's next to next's clone's next
        # loop each node, use its random
        
        if not head: return None
        
        hash = {}
        curr = head
        
        while curr:
            hash[curr] = Node(curr.val)
            curr = curr.next
            
        curr1 = head
        
        while curr1:
            if curr1.next:
                hash[curr1].next = hash[curr1.next]
            if curr1.random:
                hash[curr1].random = hash[curr1.random]
            curr1 = curr1.next
        
        return hash[head] 
        
        
        
        

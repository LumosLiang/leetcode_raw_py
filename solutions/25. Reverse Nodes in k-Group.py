# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def reverseKGroup(self, head, k):
        
        if k is None: return None
        
        # base
        curr = head
        for _ in range(k):
            if curr is None: return head
            curr = curr.next
        
        self.successor = ListNode()
        new_head = self.reverseFirstK(head, k)
        nxt = self.reverseKGroup(self.successor, k)
        head.next = nxt
        return new_head
        
    def reverseFirstK(self, head, k):
        if k == 1:
            self.successor = head.next
            return head
            
        first = self.reverseFirstK(head.next, k - 1)
        head.next.next = head
        head.next = self.successor
        return first
​
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head: return None
        
        if not head.next: return head
        
        pre, curr, nxt = None, head, None
        head = head.next 
        
        while curr and curr.next:
            nxt = curr.next
            if pre:
                pre.next = nxt
            curr.next = nxt.next
            nxt.next = curr
            pre = curr
            curr = curr.next
            
        return head
        

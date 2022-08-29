# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next: return head
        
        dummy = ListNode(-102)
        
        pre, curr, nxt = None, head, None
        p = dummy
        
        while curr:
            nxt = curr.next
            if (not pre and nxt and curr.val != nxt.val) or (not nxt and pre and curr.val != pre.val) or (nxt and pre and curr.val != nxt.val and curr.val != pre.val):
                p.next = ListNode(curr.val)
                p = p.next
                
            pre = curr
            curr = curr.next
            
        return dummy.next

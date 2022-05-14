# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursive(head)
        
    def iterative(self, head):
        
        # dummy -> 1 -> 2 -> 3
        # dummy -> 2 -> 1 -> 3
        
        dummy = ListNode()
        dummy.next = head
    
        pre, curr, nxt = dummy, head, None
        
        while curr and curr.next:
            # curr node's next node
            nxt = curr.next
            # next node's next node - nxt_nxt
            nxt_nxt = nxt.next
            
            # set the prev node's next to next node
            pre.next = nxt
            # set the prev node's next to curr node - swap
            nxt.next = curr
            # set the curr node's next to new next node
            curr.next = nxt_nxt
            
            # move to next state
            pre = curr
            curr = curr.next
        
        return dummy.next
        
    
    # post-order
    def recursive(self, head):
       
        if not head or not head.next: return head
        
        nxt_pair_h = self.recursive(head.next.next)
        
        nh = head.next
        nh.next = head
        head.next = nxt_pair_h
        
        return nh
        
        

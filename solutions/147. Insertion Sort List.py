# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        dummy.next = head
        
        pre, curr = head, head.next
        
        while curr:
            nxt = curr.next
            
            start, end = dummy, dummy.next
            
            while end and end.val < curr.val:
                start = end
                end = end.next
            
            if end != curr:
                start.next = curr
                curr.next = end
                
                pre.next = nxt
                curr = nxt
            else:
                pre = curr
                curr = nxt
                
        return dummy.next

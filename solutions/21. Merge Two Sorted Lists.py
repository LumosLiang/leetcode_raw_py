# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1, curr2 = l1, l2
        dummy = ListNode()
        curr = dummy
        
        if not l1 or not l2: return l1 or l2
        
        while curr1 and curr2:
            if curr1.val >= curr2.val:
                curr.next = curr2
                curr2 = curr2.next
            else:
                curr.next = curr1
                curr1 = curr1.next
            curr = curr.next
            
        if curr1: curr.next = curr1
        else: curr.next = curr2
            
        return dummy.next

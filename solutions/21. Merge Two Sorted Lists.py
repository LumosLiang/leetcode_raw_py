# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
<<<<<<< HEAD
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(-1)
        curr1, curr2, curr3 = l1, l2, dummy

        while curr1 and curr2:
            if curr1.val >= curr2.val:
                curr3.next = curr2
                curr2 = curr2.next
            else:
                curr3.next = curr1
                curr1 = curr1.next
            curr3 = curr3.next

        curr3.next = curr2 if not curr1 else curr1

        return dummy.next
=======
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
>>>>>>> 1870dd3c764dee6f244fb461499fe34e38527ffd

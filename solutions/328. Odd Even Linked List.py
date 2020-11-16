# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None: return None
        len1 = 0
        curr1,curr2 = head, head.next
        curr3,curr4 = head.next, head
        
        while curr4:
            curr4 = curr4.next
            len1 += 1
        
        if len1%2 == 0:
            while curr2.next:
                curr1.next = curr2.next
                curr1 = curr1.next
                curr1, curr2 = curr2, curr1
​
            curr1.next = curr3
            return head
        else:
            while curr1.next:
                curr1.next = curr2.next
                curr1 = curr1.next
                curr1, curr2 = curr2, curr1
​
            curr1.next = curr3
            return head
            
            
        
​

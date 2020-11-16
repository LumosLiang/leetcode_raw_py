# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = curr = head
        
        while curr:
            if curr.val != val:
                pre = curr
                curr = curr.next
            else:
                if curr == head:
                    head = curr.next
                    pre = curr = head
                else:
                    pre.next = curr.next
                    curr = curr.next
        
        return head
        

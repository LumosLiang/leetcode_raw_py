# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.solution1(head)
   
    # recursive
    # O(N), O(N)
    def solution1(self, head):
        
        if not head or not head.next: return head
        nh = self.solution1(head.next)
        head.next.next = head
        head.next = None
        
        return nh
        
    # O(N), O(1)
    def solution2(self, head):
        
        
        pre, curr, nxt = None, head, None
        
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        
        
        return pre

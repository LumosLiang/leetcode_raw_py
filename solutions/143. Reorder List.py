# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def reorderList(self, head: ListNode) -> None:
​
​
        if head is None: return None
​
        def rev(head):
            pre, curr, nxt = None, head, None
            
            while curr:
                nxt = curr.next
                curr.next = pre
                pre = curr
                curr = nxt
            
            return pre
​
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
​
        sec_h = rev(slow.next)
        slow.next = None
​
        curr = head
        while sec_h:
            nxt = curr.next
            curr.next = sec_h
            curr = sec_h
            sec_h = nxt
​
        return head
​
            

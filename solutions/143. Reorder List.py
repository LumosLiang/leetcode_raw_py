# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # O(N), O(N)
        # convert to list, then reorder, then convert back to linked list
        
        # 1, 2, 
        # 4, 3, 
        # O(N), O(1)
        
        # find middle
        slow, fast = head, head
        # find left middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        sec_half_head = slow.next
        slow.next = None
        
        # reverse
        pre, curr, nxt = None, sec_half_head, None
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        
        # two pointers
        p1, p2 = head, pre
        while p2:
            nxt = p1.next
            p1.next = p2
            p1 = p1.next
            p2 = nxt
        
        return head
        
        
        
        
        

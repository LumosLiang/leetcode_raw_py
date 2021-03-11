# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
​
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if not head: return None
        
        slow, fast = head, head
        
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow: break
        
        if fast is None or fast.next is None: return None
        
        slow = head
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
        
        
        
        
        

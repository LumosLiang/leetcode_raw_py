# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if head is None: return None
        
        pre, slow, fast = None, head, head
        temp = 1
        
        while temp < k:
            fast = fast.next
            temp += 1
        
        pre = fast
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.val, pre.val = pre.val, slow.val    
        
        return head
        

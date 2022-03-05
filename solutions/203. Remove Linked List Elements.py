# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        return self.sol2(head, val)
        
    # O(N), O(1)  
    def sol1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        pre = ListNode()
        pre.next = head
        curr = pre
        
        while curr.next:
            if curr.next.val == val: curr.next = curr.next.next
            else: curr = curr.next
        
        return pre.next
    
    # O(N), O(N)(stack space) 
    def sol2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if not head: return None
        
        if head.val == val:
            head = self.sol2(head.next, val)
        else:
            head.next = self.sol2(head.next, val)
        
        return head
        
​

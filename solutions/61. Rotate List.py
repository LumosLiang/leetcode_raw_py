# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
​
        return self.sol1(head, k)
    
    def sol1(self, head, k):
        if not head: return None
​
        l = 1
        curr = head
        
        while curr.next:
            curr = curr.next
            l += 1
        
        if k == l: return head
        
        tail = curr
        k = k % l
        
        if not k: return head
        
        cnt = 0
        curr = head
        
        while cnt < l - k - 1:
            curr = curr.next
            cnt += 1
    
        nh = curr.next
        curr.next = None
        tail.next = head
        
        return nh
        
        

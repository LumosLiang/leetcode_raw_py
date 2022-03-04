# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.sol2(head)
​
    # O(N), O(1)
    def sol1(self, head):
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow: return True
        
        return False
​
    # O(N), O(N)
    def sol2(self, head):
        
        h, curr = {}, head
        
        while curr:
            if curr in h:
                return True
            else:
                h[curr] = curr.val
                curr = curr.next
                
        return False

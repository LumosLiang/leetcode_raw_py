# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
# O(1) space
​
#艹 原来这里用的是中间
class Solution:
    def isPalindrome(self, head):
        
        def reverse(node):
            prev, curr, next = None, node, None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
​
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid_rev = reverse(slow)
        
        start = head
        while mid_rev:
            if start.val != mid_rev.val:
                return False
            start = start.next
            mid_rev = mid_rev.next
​
        return True
        
        
        
            
        
        
            
        
        
        
            
            
            
        
        
        
        

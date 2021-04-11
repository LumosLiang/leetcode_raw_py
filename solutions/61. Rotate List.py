# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head: return None
        
        length = 0 
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        k = k % length
        
        if k == 0:
            return head
        else:
            slow_pre, slow, fast = None, head, head
            temp = 1
            while temp < k:
                fast = fast.next
                temp += 1
​
            while fast.next:
                slow_pre= slow
                slow = slow.next
                fast = fast.next
​
            fast.next = head
            slow_pre.next = None
​
            return slow
        
​

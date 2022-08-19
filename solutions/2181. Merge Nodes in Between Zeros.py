# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        
        # prefix sum
        curr, nxt = head, None
        
        while curr.next:
            nxt = curr.next
            nxt.val += curr.val
            curr = curr.next
        
        
        # start
        
        curr, nxt, pre_sum, curr_d = head, None, 0, dummy
        
        while curr.next:
            nxt = curr.next
            if curr.val == nxt.val:
                temp = curr.val - pre_sum
                curr_d.next = ListNode(temp)
                curr_d = curr_d.next
                pre_sum = curr.val
            curr = curr.next
        
        return dummy.next

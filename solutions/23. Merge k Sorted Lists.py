# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
​
        if not lists: return 
        
        if len(lists) == 1: return lists[0]
        
        lo, hi = 0, len(lists) - 1
        mid = lo + (hi - lo) // 2
        left = self.mergeKLists(lists[:mid + 1])
        right = self.mergeKLists(lists[mid + 1:])
        
        return self.merge(left, right)
        
        
    def merge(self, l1, l2):
        
        if not l1: return l2
        if not l2: return l1
        
        dummy = ListNode(-1)
        curr1, curr2, curr3 = l1, l2, dummy
        
        while curr1 and curr2:
            if curr1.val >= curr2.val:
                curr3.next = curr2
                curr2 = curr2.next
            else:
                curr3.next = curr1
                curr1 = curr1.next
            curr3 = curr3.next
        
        curr3.next = curr2 if not curr1 else curr1
        
        return dummy.next
    

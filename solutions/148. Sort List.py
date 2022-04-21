# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
​
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # merge sort -> 
​
            # preorder traversal
            # first locate mid
            # then DC
            # then merge
​
        # iterative merge sort
            # set a k, and increase k at the appro time
            # merge first k, then next k
            # merge those k
        
        # O(NlogN), O(logN)
        # quick sort
        # pick the first as one as pivot
​
        if not head or head.next == None: return head
​
        dummy, small, large = ListNode(), ListNode(), ListNode()
        pivot = head.val
        d, s, l, curr = dummy, small, large, head.next
​
        while curr:
            if curr.val < pivot:
                s.next = curr
                s = s.next
            else:
                l.next = curr
                l = l.next
            curr = curr.next
​
        s.next = None
        l.next = None
​
        left = self.sortList(small.next)
        right = self.sortList(large.next)
​
        if left:
            currl = left
            while currl.next: currl = currl.next
            currl.next = head
            head.next = right

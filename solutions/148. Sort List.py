# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.quicksort(head)
    
    # O(NlogN), O(logN)
    # quick sort
    
    def quicksort(self, head):
        
        if not head or not head.next: return head
        
        # pick pivot, randomly
        length = 0
        curr = head
        h = []
        while curr:
            h.append(curr) 
            length += 1
            curr = curr.next
        pivot_node_idx = random.randint(0, length - 1)
        pivot_node = h[pivot_node_idx]
        pivot_val = pivot_node.val

        # generate linked list < pivot, = pivot, and > pivot
        l, r, m = ListNode(), ListNode(), ListNode()
        curr, lcurr, rcurr, mcurr = head, l, r, m
        
        while curr:
            if curr.val < pivot_val:
                lcurr.next = curr
                lcurr = lcurr.next
            elif curr.val > pivot_val:
                rcurr.next = curr
                rcurr = rcurr.next
            else:
                mcurr.next = curr
                mcurr = mcurr.next
            curr = curr.next
    
        # processing node.
        mcurr.next = None
        lcurr.next = None
        rcurr.next = None
        
        # divide and conquer
        left = self.quicksort(l.next)
        right = self.quicksort(r.next)
        
        # link them all
        mcurr.next = right
        if not left: return m.next

        left_end = left
        while left_end.next: left_end = left_end.next
        left_end.next = m.next
        return left

    def merge_sort(self, head):
        
#         fast/slow -> mid
#         mergesort(left)
#         mergesort(right)
        
#         return merge(left, right)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # This can be acheived in-place or not in-place
        return self.inplace(head)
    
    # O(N), O(1)
    def inplace(self, head):
        
        dummyN = ListNode(-101)
        dummyN.next = head
        
        pre, curr, nxt = dummyN, head, None
        
        while curr:
            nxt = curr.next
            if curr.val == pre.val:
                pre.next = nxt
            else:
                pre = curr
            curr = nxt
        
        return dummyN.next
        
    # O(N), O(N)
    def notinplace(self, head):
        
        curr, lst = head, []
        
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        l, r = 0, 0
        
        while r < len(lst):
            if lst[r] != lst[l]:
                lst[l + 1] = lst[r]
                l += 1
            r += 1
        
        lst = lst[:l + 1]
        
        dummyN = ListNode()
        curr = dummyN
        
        for num in lst:
            curr.next = ListNode(num)
            curr = curr.next
        
        return dummyN.next
        
        

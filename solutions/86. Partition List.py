class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
     
        if not head: return None
        
        less = ListNode(None)
        greater = ListNode(None)
        
        curr_less, curr_greater, curr = less, greater, head
        
        while curr:
            if curr.val < x:
                curr_less.next = ListNode(curr.val)
                curr_less = curr_less.next
            else:
                curr_greater.next = ListNode(curr.val)
                curr_greater = curr_greater.next
            curr = curr.next
            
        curr_less.next = greater.next
        return less.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # O(N), O(N) -> easy
        
    
        # O(N), O(1)
        
        # 1. use k loop
        # 2. connect all the odd node, and even nodes in this k loop
        # 3. and must do it together
    
        # 1 -> 3  -> 5
        # 2 -> 3
        # 4 -> 5
        
        return self.sol2(head)
    
    # single pointer
    def sol1(self, head):
        if not head or not head.next: return head
​
        odd_head = head
        even_head = head.next
            
        pre, curr, nxt = head, head.next, None
        flag = False
        
        while curr.next:
            nxt = curr.next
            pre.next = nxt
            pre = curr
            curr = nxt
            flag = not flag
            
        if flag:
            pre.next = None
            curr.next = even_head
        else:
            pre.next = even_head
​
        return odd_head
​
    
    # double pointer
    def sol2(self, head):
        if not head: return head
        
        even_head = head.next
        odd, even = head, even_head
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = even_head
        return head
            

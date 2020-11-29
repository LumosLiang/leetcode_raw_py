# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head: return head
        
        pre, curr, nxt = None, head, None
        
        while curr.next:
            nxt = curr.next
            if curr.val != nxt.val:
                pre = curr
                curr = nxt
            else:
                while nxt.val == curr.val: 
                    if nxt.next:
                        nxt = nxt.next
                    else:
                        nxt = None
                        break
                        
                if pre and nxt:       
                    pre.next = nxt
                    curr = nxt
                elif not pre and not nxt:
                    return None
                elif not pre and nxt:
                    head = nxt
                    curr = nxt
                elif pre and not nxt:
                    pre.next = nxt
                    return head
        return head
                  

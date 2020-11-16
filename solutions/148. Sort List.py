# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
​
# recursive
​
# iterative
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None: return None
        
        p1, p2 = head, head.next
        smallest = head    
        nxt = None
        
        while p2:
            nxt = p2.next
            if p1.val <= p2.val:
                p1.next = p2
                p1 = p2
                p2 = nxt
            else:
                p1.next = None
                if p2.val >= smallest.val:
                    temp = smallest.next
                    temp_pre = smallest
                    while temp:
                        if p2.val < temp.val:
                            break
                        else:
                            temp_pre = temp
                            temp = temp.next
                    p2.next = temp
                    temp_pre.next = p2
                else:
                    p2.next = smallest
                    smallest = p2
                p2 = nxt
                
        return smallest
                
                
        
        
            
            
        
        
        
        
        

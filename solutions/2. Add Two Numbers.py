# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
​
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        len1, len2 = 0, 0
        curr1, curr2 = l1, l2
        
        while curr1:
            curr1 = curr1.next
            len1 += 1
        
        while curr2:
            curr2 = curr2.next
            len2 += 1
        
        
        def helper(l1, l2, len1):
            # assume len(l1) > len(l2)
            ans, curr1, curr2 = l1, l1, l2
            end, pre, nxt = 0, 0, 0
​
            while curr1:
                end += 1
​
                if curr2:
                    val = curr1.val + curr2.val + pre
                    curr2 = curr2.next
                else:
                    val = curr1.val + pre
​
                if val >= 10:
                    l1.val = val - 10
                    nxt = 1 
                else:
                    l1.val = val
                    nxt = 0
​
                pre = nxt
                curr1 = curr1.next
​
                if end != len1:
                    l1 = l1.next
​
            if pre == 1:
                l1.next = ListNode(pre)
​
            return ans     
                
        if len1 >= len2:
            return helper(l1, l2, len1)
        else:
            return helper(l2, l1, len2)
              
        

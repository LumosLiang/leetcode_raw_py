# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # O(N), O(N)
        
        # get length
        def compute_len(head):
            cnt = 0
            while head:
                head = head.next
                cnt += 1
            return cnt
        
        # swap based on length
        len1, len2 = compute_len(l1), compute_len(l2)
        
        len_diff = abs(len1 - len2)
        
        if len1 < len2: l1, l2 = l2, l1
        
        # take a stack to do the backward plus
        cnt, stack = 0, []
        curr1, curr2 = l1, l2
        
        # keep the two pointer start at the same pos
        while cnt < len_diff:
            stack.append(curr1.val)
            curr1 = curr1.next
            cnt += 1
            
        # start compute
        while curr1:
            s = curr1.val + curr2.val
            if s < 10:
                stack.append(s)
            else:
                temp = [s % 10]
                while stack and stack[-1] + 1 >= 10:
                    last = stack.pop()
                    temp.append((last + 1) % 10)
                
                if not stack: stack = [1]
                else: stack[-1] += 1
                stack += temp[::-1]
                
            curr1 = curr1.next
            curr2 = curr2.next
    
        # build the linked list
        dummy = ListNode(-1)
        curr = dummy
        for s in stack:
            curr.next = ListNode(s)
            curr = curr.next
        return dummy.next
        

​
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.sol2(l1, l2)
    
    # two pointers,
    # if > 10, take one-digit, record ten-digit
    
    # merge
    # O(N + M), O(N + M)
    def sol1(self, l1, l2):
        
        p1, p2 = l1, l2
        dummy = ListNode()
        p3 = dummy
        carry = 0
        
        while p1 or p2:
            temp_sum = carry
            if p1:
                temp_sum += p1.val
                p1 = p1.next
            if p2:
                temp_sum += p2.val
                p2 = p2.next
            p3.next = ListNode(temp_sum % 10)
            carry = temp_sum // 10
            p3 = p3.next
           
        p3.next = ListNode(carry) if carry else None
        
        return dummy.next
    
    # recursion
    # O(N + M), O(N + M)
    def sol2(self, l1, l2):
        
        dummy = ListNode(-1)
        p3 = dummy
        
        def helper(l1, l2, ten_digt, p3):
            if not l1 and not l2 and not ten_digt: return
            
            temp_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + ten_digt
            p3.next = ListNode(temp_sum % 10)
            
            if l1 and l2:    
                helper(l1.next, l2.next, temp_sum // 10, p3.next)
            elif l1:
                helper(l1.next, None, temp_sum // 10, p3.next)
            elif l2:
                helper(None, l2.next, temp_sum // 10, p3.next)
        
        helper(l1, l2, 0, p3)
        return dummy.next
    

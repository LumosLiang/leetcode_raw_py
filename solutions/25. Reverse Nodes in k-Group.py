# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def reverseKGroup(self, head, k):
        
        return self.recursive(head,k)
​
    # O(N), O(N//k)
    def recursive(self, head, k):
        if not head: return None
    
        cnt = 1
        curr = head
        
        while curr and cnt < k:
            cnt += 1
            curr = curr.next
        
        if not curr: return head
        
        nxt = curr.next
        curr.next = None
        nh = self.reverse(head)
        
        head.next = self.reverseKGroup(nxt, k)
        
        return nh
    
    # O(k), O(1)
    def reverse(self, head):
        if not head: return None
        
        pre, curr, nxt = None, head, None
        
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        
        return pre
    
    # O(N), O(1)
​
    # dummy
​
    # 每一次我都取n, n+k的node， 
    # start, trail
    # 但是同时，要记录，该段翻转的前一个点和后一个点，pre, tnxt.
    # in-place reverse: 注意的点就是要，确定好新的 head, 和tail
​
    # start.pre.next = trail.
    # start.next = trail.next
    # 再次记录头
​
    # 取下一组K，
​
    # 如果取不到，就直接return dummy.next
​
    # 如果题目要求是 无论不足也翻转的话，那这种事情，应该只出现一次，就是在最后一组。
    # 如果遇到取不到k，
    # 就也翻转一次。
​
    def iterative(self, head, k):
        
        pass
        
            

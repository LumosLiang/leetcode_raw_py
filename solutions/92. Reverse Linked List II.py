class Solution:
    def reverseBetween(self, head, m, n):
    
        if m == 1:
            self.successor = ListNode()
            return self.helper(head, n)
​
        first = self.reverseBetween(head.next, m - 1, n - 1)
        head.next = first
        return head
​
    def helper(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        
        start = self.helper(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return start

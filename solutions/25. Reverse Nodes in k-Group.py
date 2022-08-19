# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        return self.iterative(head, k)
    
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
    
    # follow-up1: require to reverse even if the number of nodes is not a multiple of k
    def followup1(self, head, k):
        
        if not head: return None
        
        curr, cnt = head, 0
        
        while curr and cnt < k - 1:
            curr = curr.next
            cnt += 1
        
        if not curr: return self.reverse(head)
        
        nxt = curr.next
        curr.next = None
    
        new_nxt = self.followup1(nxt, k)
        nh = self.reverse(head)
        head.next = new_nxt
        
        return nh
    
    # follow-up2, do this from the tail
    def followup2(self, head, k):
        if not head: return None
        
        def reversebykgroup(head, k):
            if not head: return None
    
            cnt = 0
            curr = head

            while cnt < k - 1:
                cnt += 1
                curr = curr.next

            nxt = curr.next
            curr.next = None
            nh = self.reverse(head)

            head.next = self.reverseKGroup(nxt, k)

            return nh
        
        cnt, curr = 0, head
        while curr:
            cnt += 1
            curr = curr.next
        
        skip = cnt % k
    
        cnt, curr = 0, head
        while cnt < skip - 1:
            cnt += 1
            curr = curr.next
        
        curr.next = reversebykgroup(curr.next, k)
        return head

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
    # # [1,2,3,4,5,6,7,8] 3
    
    #    dummy -> 1 -> 2 -> 3
#          curr   tail  
#          2,1,3,4,5,6,7,8
#     #    3,2,1,4,5,6,7,8
#     #    3,2,1,5,4,6,7,8
#     #    3,2,1,6,5,4,7,8
#     #    3,2,1, 6,5,4, 7,8
    
    def iterative(self, head, k):
        
        if not head: return None
        
        cnt, curr = 0, head
        while curr:
            cnt += 1
            curr = curr.next
        
        group_cnt = cnt // k
        
        dummy = ListNode
        dummy.next = head
        curr = dummy
        
        for _ in range(group_cnt):
            tail = curr.next
            for _ in range(k - 1):
                temp = curr.next
                curr.next = tail.next
                tail.next = tail.next.next
                curr.next.next = temp
            
            curr = tail
            
        return dummy.next

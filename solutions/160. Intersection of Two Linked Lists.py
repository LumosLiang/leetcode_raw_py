# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        return self.sol0(headA, headB)
    
    # brute force + TLE
    def sol0(self, headA: ListNode, headB: ListNode):
        
        c1= headA
        
        while c1:
            c2 = headB
            while c2:
                if c1 == c2:
                    return c1
                c2 = c2.next
            c1 = c1.next
        return None
    
    # O(M+N), O(M+N)
    # hash
    def sol1(self, headA: ListNode, headB: ListNode):
        
        c1, c2 = headA, headB
        s = set()
        
        while c1:
            if c1 not in s:
                s.add(c1)
            c1 = c1.next
        
        while c2:
            if c2 in s:
                return c2
            c2 = c2.next
        return None
    
    # O(M+N), O(1)
    # two pointer: fast, slow
    def sol2(self, headA: ListNode, headB: ListNode):
        
        # 1 length
        def cal_len(head):
            if not head: return 0
            curr, cnt = head, 0
            while curr:
                curr = curr.next
                cnt += 1
            return cnt
        
        # 2 make the same length start O(M + N)
        cntA, cntB = callen(headA), callen(headB)
        
        if cntA > cntB:
            while cntA - cntB:
                headA = headA.next
                cntA -= 1
        else:
            while cntB - cntA:
                headB = headB.next
                cntB -= 1
        
        # 3 start

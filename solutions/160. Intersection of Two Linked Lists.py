# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        lenA = lenB = 0
        currA = headA
        currB = headB
        
        while currA:
            currA = currA.next
            lenA += 1
        
        while currB:
            currB = currB.next
            lenB += 1
        
        currA = headA
        currB = headB
        if lenA > lenB:
            while lenA - lenB > 0:
                lenA -= 1
                currA = currA.next
        else:
            while lenB - lenA > 0:
                lenB -= 1
                currB = currB.next
        
        while currA:
            if currA is currB:
                return currA
            else:
                currA = currA.next
                currB = currB.next
        

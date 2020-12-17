# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        
        curr1 = list1
        curr2 = list2
        temp1, tempa = 0, 0
        
        while curr1:
            if temp1 == a - 1:
                break
            curr1 = curr1.next
            temp1 += 1
        
        curra = curr1.next
        while curra:
            if tempa == b - temp1 - 1:
                break
            curra = curra.next
            tempa += 1
        
        currb = curra.next
        
        while curr2.next:
            curr2 = curr2.next
            
        curr1.next = list2
        curr2.next = currb
        
        return list1
        
            
        

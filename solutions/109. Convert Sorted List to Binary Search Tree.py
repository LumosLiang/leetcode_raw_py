# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
# DFS? 
​
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
​
        if head is None: return None
        
        if head.next is None : return TreeNode(head.val)
        
        pre, slow, fast = None, head, head
        
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        pre.next = None
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root
        
        
        
        
        
        
        
            
            

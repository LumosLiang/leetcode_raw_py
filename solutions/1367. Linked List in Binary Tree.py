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
class Solution:
    
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        def subpath(head, root):
            if not head: return True
            if not root: return False
            if head.val == root.val:
                return subpath(head.next, root.left) or subpath(head.next, root.right)
        
        if not head: return True
        if not root: return False
        if subpath(head, root): return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        
        
  
       
        

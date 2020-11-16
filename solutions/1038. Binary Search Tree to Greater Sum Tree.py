# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
# Reverse in-order
​
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None: return 0
​
        val = 0
        head = root
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.right      
            else:
                node = stack.pop()
                node.val += val
                val = node.val
                root = node.left
                
        return head
        
        

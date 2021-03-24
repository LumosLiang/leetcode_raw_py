# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
# iterative
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None: return
        
        q = [root]
        
        while q:
            temp = q.pop()
            if temp.left:
                q.insert(0, temp.left)
            if temp.right:
                q.insert(0, temp.right)
            temp.left, temp.right = temp.right, temp.left
        return root
            

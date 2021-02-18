# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def buildTree(self, inorder, postorder):
        
        if postorder == []: return None
        if len(postorder) == 1: return TreeNode(postorder[0])
        
        root_val = postorder[-1]
        idx = inorder.index(root_val)
        
        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: return None
        if p == root or q == root: return root
        
        left_LCA = self.lowestCommonAncestor(root.left, p, q)
        right_LCA = self.lowestCommonAncestor(root.right, p, q)
        
        if left_LCA and right_LCA: return root
        else: return right_LCA or left_LCA

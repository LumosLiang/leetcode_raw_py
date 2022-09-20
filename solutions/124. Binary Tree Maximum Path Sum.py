# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = float('-inf')
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        self.get_sum(root)
        
        return self.res
        
    def get_sum(self, root):
        
        if not root: return 0
        
        ls = self.get_sum(root.left)
        rs = self.get_sum(root.right)
        
        self.res = max(self.res, root.val, root.val + ls, root.val + rs, root.val + ls + rs)
        
        return max(root.val, root.val + ls, root.val + rs)

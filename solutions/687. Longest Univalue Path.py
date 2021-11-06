# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        def helper(root):
            
            if not root: return 0
            
            lc = helper(root.left)
            rc = helper(root.right)
            
            lc = (lc + 1) if root.left and root.left.val == root.val else 0
            rc = (rc + 1) if root.right and root.right.val == root.val else 0
            
            tempc = max(lc, rc)
            self.res = max(self.res, lc + rc)
            
            return tempc
        
        helper(root)
        return self.res

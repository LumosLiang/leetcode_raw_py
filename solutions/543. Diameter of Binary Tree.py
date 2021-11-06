# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def helper(root):
            
            if not root: return (0, 0)
            
            lc, lstopsum = helper(root.left)
            rc, rstopsum = helper(root.right)
            
            tempc = max(1, 1 + lc, 1 + rc)
            tempstopsum = max(tempc, lstopsum, rstopsum, lc + rc + 1)
            
            return (tempc, tempstopsum)
        
        return helper(root)[1] - 1
        

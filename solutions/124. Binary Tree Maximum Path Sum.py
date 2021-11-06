# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        # helper func return (pathsum that need to be continuly computed, existing largest path sum)
        def helper(root):
            
            if not root: return (float('-inf'), float('-inf'))
            
            lc, lstopsum = helper(root.left)
            rc, rstopsum = helper(root.right)
            
            return (max(root.val, root.val + lc, root.val + rc), max(root.val, root.val + lc, root.val + rc, lstopsum, rstopsum, lc + rc + root.val))
        
        return helper(root)[1]
​

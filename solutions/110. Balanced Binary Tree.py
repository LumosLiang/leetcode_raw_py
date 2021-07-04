# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def helper(root):
            
            if root is None: return [True, 0]
            
            isBL, LH = helper(root.left)
            isBR, RH = helper(root.right)
        
            if isBL and isBR:
                if abs(LH - RH) <= 1: return [True, max(LH, RH) + 1]
                else: return [False, max(LH, RH) + 1]
            else:
                return [False, max(LH, RH) + 1]
        
        
        return helper(root)[0]

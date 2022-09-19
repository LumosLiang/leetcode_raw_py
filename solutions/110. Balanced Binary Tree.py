# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        # return height and isBalanced
        def helper(root):
            
            if not root: return (True, 0)
            
            is_BLT_left, lh = helper(root.left)
            is_BLT_right, rh = helper(root.right)
​
            if is_BLT_left and is_BLT_right and abs(lh - rh) <= 1:
                return (True, max(lh, rh) + 1)
            
            return (False, 0)
        
        return helper(root)[0]
            
            
            
            

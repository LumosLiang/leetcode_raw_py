# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        if root is None: return None
        
        res, isinc_t = self.helper(root, target)
        
        if not isinc_t:
            return res
        
        return self.removeLeafNodes(res, target)
        
    def helper(self, root, target):
        if root is None: return None, False
​
        if root.val == target and not root.left and not root.right:
            return None, False
​
        root.left, inc_t_l = self.helper(root.left, target)
        root.right, inc_t_r = self.helper(root.right, target)
​
        return root, (root.val == target and not root.left and not root.right) or inc_t_l or inc_t_r
        
        
            
        
        
        

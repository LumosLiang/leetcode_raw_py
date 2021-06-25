# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        
        if root is None: return None
        
        if root.val > high or root.val < low:
            if root.val < low: return self.trimBST(root.right, low, high)
            else: return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root
        
        

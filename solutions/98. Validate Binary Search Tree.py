# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
​
​
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # cannot just simply compare left and right and root
        
        return self.ValidBST(root, None, None)
    
    def ValidBST(self, root, left_b, right_b):
        if root is None: return True
        if left_b and root.val <= left_b.val: return False
        if right_b and root.val >= right_b.val: return False
​
        return self.ValidBST(root.left, left_b, root) and self.ValidBST(root.right, root, right_b)
​
            
            
        
        

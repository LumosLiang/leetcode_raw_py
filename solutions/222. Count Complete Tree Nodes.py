# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        if not root: return 0
        lh = self.countHeight(root.left)
        rh = self.countHeight(root.right)
        
        if lh == rh:
            return 2 ** lh + self.countNodes(root.right)
        else:
            return 2 ** rh + self.countNodes(root.left)
​
        
        
    def countHeight(self, root):
        if not root: return 0
        return 1 + self.countHeight(root.left)
​

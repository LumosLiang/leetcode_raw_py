# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        # recursive
     
        if t1 is None and t2 is not None:
            new_node = TreeNode(t2.val, t2.left, t2.right)
            return new_node
        elif t2 is None and t1 is not None:
            new_node = TreeNode(t1.val, t1.left, t1.right)
            return new_node
        elif t1 and t2:
            new_node = TreeNode(t1.val + t2.val, self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right))
            return new_node
     

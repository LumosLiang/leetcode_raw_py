# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right、
​
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
      
        lst = []
        def inorder(root):
            if root.left: inorder(root.left)
            lst.append(root.val)
            if root.right: inorder(root.right)
       
        inorder(root)
        return min(b - a for a, b in zip(lst, lst[1:])) 

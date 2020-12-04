# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
# recusive
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
       
        if not root: return TreeNode(val)
        
        if root.val > val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                self.insertIntoBST(root.left, val)
            else:
                root.right = TreeNode(val)
        
        return root
         

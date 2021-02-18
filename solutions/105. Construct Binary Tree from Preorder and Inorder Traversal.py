# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def buildTree(self, preorder, inorder):
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i
        
        def buildT(low, high):    
            if low > high: return None
            root = TreeNode(preorder.pop(0))
            idx = map_inorder[root.val]
​
            root.left = buildT(low, idx - 1)
            root.right = buildT(idx + 1, high)
            return root
            
        return buildT(0, len(inorder) - 1)
    
​

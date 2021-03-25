# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
  
class Solution:
    def buildTree(self, inorder, postorder):
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i
        
        def buildT(low, high):    
            if low > high: return None
            root = TreeNode(postorder.pop())
            idx = map_inorder[root.val]
​
            
            root.right = buildT(idx + 1, high)
            root.left = buildT(low, idx - 1)
            return root
            
        return buildT(0, len(inorder) - 1)
    
​
​
​

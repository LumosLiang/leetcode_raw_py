# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
# recursive
​
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def DFS(node, isleft = False):
            
            if node is None: return 0
            
            if node.left and node.right:  
                return DFS(node.left, True) + DFS(node.right, False)
            if not node.left and not node.right:
                return node.val if isleft else 0          
            if not node.left and node.right:
                return DFS(node.right, False)
            if not node.right and node.left:
                return DFS(node.left, True)
            
        return DFS(root)
        
        
        

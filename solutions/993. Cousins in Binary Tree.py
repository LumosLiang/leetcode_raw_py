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
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, d, p, t):
            if node:
                if node.val == t:
                    return d, p 
                return dfs(node.left, d + 1, node, t) or dfs(node.right, d + 1, node, t)
​
        dx, px = dfs(root, 0, None, x) 
        dy, py = dfs(root, 0, None, y)
        return dx == dy and px != py  
​
​
        
        
    
        

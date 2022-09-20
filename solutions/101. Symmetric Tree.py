# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    
    
        # BFS 不说了
        # DFS
        
        if not root: return None
        
        def helper(node1, node2):
            
            if not node1 and not node2: return True
            
            if node1 and node2 and node1.val == node2.val:
                return helper(node1.left, node2.right) and helper(node1.right, node2.left)
​
            return False
        
        return helper(root.left, root.right)

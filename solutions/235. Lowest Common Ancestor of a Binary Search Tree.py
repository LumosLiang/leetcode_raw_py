# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.sol2(root, p, q)
    
    # recursive的方法
    # O(N), O(h)
    def sol1(self, root, p, q):
        
        if not root: return None
        
        if root == p: return p
        
        if root == q: return q
        
        lca_l = self.sol1(root.left, p, q)
        lca_r = self.sol1(root.right, p, q)
        
        if lca_l and lca_r: return root
        else:
            if lca_l: return lca_l
            if lca_r: return lca_r
        
    
    
    # iterative as it is BST
    def sol2(self, root, p, q):
        
        while root:
            
            if min(p.val, q.val) <= root.val <= max(p.val, q.val):
                return root
            elif root.val < min(p.val, q.val):
                root = root.right
            else:
                root = root.left
        
        return root
        
    
    
        

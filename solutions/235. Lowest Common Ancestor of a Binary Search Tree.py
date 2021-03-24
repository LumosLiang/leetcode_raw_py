class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: return None
        
        elif p.val < root.val and q.val < root.val: return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val: return self.lowestCommonAncestor(root.right, p, q)
        return root

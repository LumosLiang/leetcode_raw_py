class Solution:
    def sumEvenGrandparent(self, root):
        self.sum = 0
        def dfs(root):
            if not root: return 0
            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        self.sum += root.left.left.val
                    if root.left.right:
                        self.sum += root.left.right.val
                if root.right:
                    if root.right.left:
                        self.sum += root.right.left.val
                    if root.right.right:
                        self.sum += root.right.right.val
            
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            
        dfs(root)
        return self.sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
      
        self.node1, self.node2, self.pre = None, None, TreeNode(float('-inf'))
        self.findFirst = False
        
        def helper(root):
            
            if not root: return
            
            helper(root.left)
            
            if root.val < self.pre.val:
                if not self.findFirst:
                    self.node1 = self.pre
                    self.findFirst = True
                
                self.node2 = root
            
            self.pre = root
            
            helper(root.right)
        
        helper(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
        

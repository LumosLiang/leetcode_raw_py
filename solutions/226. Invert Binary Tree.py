# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
# iterative
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None: return
        
        q = collections.deque([root])
        
        while q:
            temp = q.pop()
            if temp.left:
                q.appendleft(temp.left)
            if temp.right:
                q.appendleft(temp.right)
            temp.left, temp.right = temp.right, temp.left
        return root
        
    
    def invertTreeRecur(self, root: TreeNode):
        
        if not root: return
        
        left = self.invertTreeRecur(root.left)
        right = self.invertTreeRecur(root.right)
        
        root.right = left
        root.left = right
    
        return root
​
    

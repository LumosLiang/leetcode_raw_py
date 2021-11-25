# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
# recursive
​
# class Solution:
#     def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
#         if not root: return 0
        
#         if root.left and not root.left.left and not root.left.right: 
#             return root.left.val + self.sumOfLeftLeaves(root.right)
        
#         return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
​
# BFS    
    
# class Solution:
#     def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
#         res, q =  0, collections.deque([root])
        
#         while q:
#             node = q.popleft()
#             if not node: continue
#             if node.left and not node.left.left and not node.left.right: res += node.left.val
#             if node.right: q.append(node.right)
#             if node.left: q.append(node.left)
#         return res
        
​
# DFS
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        res, stack = 0, [root]
        
        while stack:
            node = stack.pop()
            if not node: continue
            if node.left and not node.left.left and not node.left.right: res += node.left.val
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return res

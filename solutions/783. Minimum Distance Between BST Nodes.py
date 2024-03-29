# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right、
​
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
      
        # self.res, self.pre = float('inf'), float('-inf')
        # self.solution1(root)
        # return self.res
    
        # return self.solution2(root, float('inf'), float('-inf'))
        return self.solution3(root)
    
    def solution1(self, root):
        
        if not root: return
        
        self.solution1(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        self.solution1(root.right)
        
    
    def solution2(self, root, high, low):
        
        if not root: return high - low
        left = self.solution2(root.left, root.val, low)
        right = self.solution2(root.right, high, root.val)
        return min(left, right)
    
    def solution3(self, root):
        lst = []
        
        def inorder(root):
            if root.left: inorder(root.left)
            lst.append(root.val)
            if root.right: inorder(root.right)
​
        inorder(root)
        return min(b - a for a, b in zip(lst, lst[1:]))      
​
        
        
        
        
        
        
        

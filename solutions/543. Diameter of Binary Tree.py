# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
#double recursion
​
class Solution:
          
    def __init__(self):
        self.res = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.sol1(root)
    
    def sol1(self, root):
        
        if not root: return 0
        
        self.depth1(root)
      
        return self.res
        
    
    # return longest path that pass through this root to one side
    def depth1(self, root):
        
        if not root: return 0
        
        l = self.depth1(root.left) 
        r = self.depth1(root.right)
        
        self.res = max(self.res, l + r)
        
        return max(1 + l, 1 + r)
    
​
    def sol2(self, root):
        
        if not root: return 0
        
        self.res = max(self.res, self.depth(root.left) + self.depth(root.right))
        
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
                    
        return self.res
        
    
    # return longest path that pass through this root to one side
    def depth(self, root):
        
        if not root: return 0
        
        return max(1 + self.depth(root.left), 1 + self.depth(root.right))

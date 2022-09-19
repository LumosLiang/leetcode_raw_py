# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.sol2(root)
    
    def sol1(self, root):
        if not root: return False
        
        def helper(root, left_bound, right_bound):
        
            if not root: return True
​
            if left_bound < root.val < right_bound:
​
                return helper(root.left, left_bound, root.val) and helper(root.right, root.val, right_bound)
​
            return False
        
        return helper(root, float('-inf'), float('inf'))
        
    
    
    def sol2(self, root):
        # iterative1
        if not root: return False
        
        res, stack, pre = [], [], float('-inf')
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val > pre:
                    pre = root.val
                    root = root.right
                else:
                    return False
        
        return True
    
    
    def sol3(self, root):
        # iterative2 
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            curr, left, right = stack.pop()
            
            if not curr: continue
            
            if left < curr.val < right:
                stack.append((curr.right, curr.val, right))
                stack.append((curr.left, left, curr.val))
            else:
                return False
        
        return True
    
        
        
        

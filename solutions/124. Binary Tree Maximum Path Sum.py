# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    
    @lru_cache(None)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # think about how you compute maximum subarray in a array
        
        # the key here is how you compute the maximum path sum through the root.
​
        # print(self.helper(root.left))
        
        if not root: return float('-inf')
        
        left_ps = self.maxPathSum(root.left)
        right_ps = self.maxPathSum(root.right)
        
        lr_ps = self.helper(root.left)
        rr_ps = self.helper(root.right)
        
        return max(root.val, root.val + lr_ps, root.val + rr_ps, root.val + lr_ps + rr_ps, left_ps, right_ps)
    
    # the maximum path sum through the root to one side
    @lru_cache(None)
    def helper(self, root):
        
        if not root: return float('-inf')
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        return max(root.val, root.val + left, root.val + right)
        
    
    
​

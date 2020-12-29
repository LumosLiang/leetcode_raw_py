# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None: return 0
        
        def helper(root, sum):
            if root is None: return 0
​
            if root.val == sum:
                rot = 1
            else:
                rot = 0
​
            left = helper(root.left, sum - root.val)
            right = helper(root.right, sum - root.val)
            return left + right + rot
​
        return helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
       
    

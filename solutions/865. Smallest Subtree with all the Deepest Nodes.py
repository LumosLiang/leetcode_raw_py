# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def helper(root, d):
            
            if not root: return [None, d - 1]
​
            if not root.left and not root.right: return [root, d]
​
            [leftlca, ld] = helper(root.left, d + 1)
            [rightlca, rd] = helper(root.right, d + 1)
​
            if ld > rd: return [leftlca, ld]
            elif ld < rd:return [rightlca, rd]
            else: return [root, ld]
​
        return helper(root, 0)[0]

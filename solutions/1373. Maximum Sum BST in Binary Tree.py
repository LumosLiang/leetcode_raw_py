# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.res = 0
        def helper(root):
            if not root: return (2, None, None, 0)
            
            isBSTl, minl, maxl, suml = helper(root.left)
            isBSTr, minr, maxr, sumr = helper(root.right)
            
            if (isBSTl == 1 and maxl < root.val or isBSTl == 2) and (isBSTr == 1 and root.val < minr or isBSTr == 2):
                self.res = max(self.res, suml + sumr + root.val)
                return (1, root.val if not minl else minl, root.val if not maxr else maxr, suml + sumr + root.val)
                
            return (0, None, None, max(suml, sumr))
           
        helper(root)
        return self.res
​

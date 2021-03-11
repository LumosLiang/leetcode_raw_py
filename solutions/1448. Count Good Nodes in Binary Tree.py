# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def countGoodNodes(curr, p, lastG):
            
            if curr is None: return 0
            
            if curr.val < p.val or curr.val >= p.val and curr.val < lastG.val:
                return countGoodNodes(curr.left, curr, lastG) + countGoodNodes(curr.right, curr, lastG)
            elif curr.val >= p.val and curr.val >= lastG.val:
                return 1 + countGoodNodes(curr.left, curr, curr) + countGoodNodes(curr.right, curr, curr)
        
        return countGoodNodes(root, root, root)

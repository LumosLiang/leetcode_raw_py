# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        if root is None: return []
        
        q, res = [root], [root.val]
        while q:
            tempn = []
            tempv = []
            while q:
                node = q.pop(0)
                if node.left:
                    tempn.append(node.left)
                    tempv.append(node.left.val)
                if node.right:
                    tempn.append(node.right)
                    tempv.append(node.right.val)
            if tempv: res.append(max(tempv))
            q = tempn
        
        return res
            

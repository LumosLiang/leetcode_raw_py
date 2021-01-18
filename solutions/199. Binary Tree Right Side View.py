# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None: return None
        
        res = [root.val]
        stack = [root]
        
        while stack:
            temp = []
            while stack:
                node = stack.pop(0)
                if node.right:
                    temp.append(node.right)
                if node.left:
                    temp.append(node.left)
            if temp:
                res.append(temp[0].val)
            stack = temp
        
        return res
            
                    
                    
                    
        
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None: return 
        
        res = [[root.val]]
        stack = [root]
        flip = True # left to right
        
        while stack:
            temp, temp_val = [], []
            while stack:
                node = stack.pop()
                if flip:
                    if node.right:
                        temp.append(node.right)
                        temp_val.append(node.right.val)
                    if node.left:
                        temp.append(node.left)
                        temp_val.append(node.left.val)
                else:
                    if node.left:
                        temp.append(node.left)
                        temp_val.append(node.left.val)
                    if node.right:
                        temp.append(node.right)
                        temp_val.append(node.right.val)
            if temp_val != []:
                res.append(temp_val)    
            stack = temp
            flip = not flip
        return res
            
            
        
        
        
        

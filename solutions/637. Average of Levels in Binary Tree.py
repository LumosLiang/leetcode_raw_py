# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None: return []
        
        res = [root.val]
        stack = [root]
        
        while stack:
            temp = []
            temp_val = []
            while stack:
                node = stack.pop()
                if node.right:
                    temp.append(node.right)
                    temp_val.append(node.right.val)
                if node.left:
                    temp.append(node.left)
                    temp_val.append(node.left.val)
            if temp_val != []:
                res.append(sum(temp_val)/len(temp_val)) 
            stack = temp
        
        return res
                    
                
                
        
        

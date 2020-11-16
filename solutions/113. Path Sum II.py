# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
# DBS
​
class Solution:
    def pathSum(self, root: TreeNode, Sum: int) -> List[List[int]]:
        
        if root is None: return []
        
        stack, path_stack, paths, res = [root], [[root.val]], [], []
        
        while stack:
            temp = stack.pop()
            path = path_stack.pop()
            
            if temp.right:
                stack.append(temp.right)
                path_stack.append(path + [temp.right.val])
            if temp.left:
                stack.append(temp.left)
                path_stack.append(path + [temp.left.val])
            if temp.right is None and temp.left is None:
                paths.append(path)
        
        print(paths)
        for item in paths:
            if sum(item) == Sum:
                res.append(item)
        return res
    
        
  
            
        
        

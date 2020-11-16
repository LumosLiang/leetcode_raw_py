# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def get_operations(root, target):
            operation = []
            stack = [root]
            
            while stack:
                temp = stack.pop()
                operation.append(0)
                if temp == target:
                    break
                else:
                    if temp.left:
                        stack.append(temp.left)
                        operation.append(-1)
                    if temp.right:
                        stack.append(temp.right)
                        operation.append(1)
            return operation
        
        steps = get_operations(original, target)
        
        s = [cloned]  
        curr = None
        while steps:
            step = steps.pop(0)
            if step == 0:
                curr = s.pop()
            elif step == -1:
                s.append(curr.left)
            elif step == 1:
                s.append(curr.right)
            
        return curr       
          
            
            
        
        
        
        
        

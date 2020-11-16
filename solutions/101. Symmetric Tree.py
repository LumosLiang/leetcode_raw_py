# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
# iteratively
​
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        stack = [root]
        ans = True
        
        while stack:
            temp = []
            
            while stack:
                temp_node = stack.pop()
                if temp_node:
                    if temp_node.left and temp_node.right:
                        temp.append(temp_node.left)
                        temp.append(temp_node.right)
​
                    if not temp_node.left and temp_node.right:
                        temp.append(None)
                        temp.append(temp_node.right)
​
                    if temp_node.left and not temp_node.right:
                        temp.append(temp_node.left)
                        temp.append(None)
                    
                    if not temp_node.left and not temp_node.right:
                        temp.append(None)
                        temp.append(None)
​
            temp_bool = True
        
            for dumy_i in range(0, int(len(temp)/2)):
                if temp[dumy_i] is not None:
                    if temp[len(temp) - 1 - dumy_i] is not None:
                        if temp[dumy_i].val != temp[len(temp) - 1 - dumy_i].val:
                            return False
                    else:
                        return False
                else:
                    if temp[len(temp) - 1 - dumy_i] is not None:
                        return False
                    
            stack = temp
        
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
#Follow up
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None: return None
        temp = 0
        
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp_node = stack.pop()
                temp += 1
                if temp == k:
                    return temp_node.val
                else:
                    root = temp_node.right
        return temp
       
                
        
        

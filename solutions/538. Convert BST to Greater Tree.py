# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
 
        if root is None: return 
​
        val = 0
        head = root
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.right      
            else:
                node = stack.pop()
                node.val += val
                val = node.val
                root = node.left
                
        return head
        
        
        

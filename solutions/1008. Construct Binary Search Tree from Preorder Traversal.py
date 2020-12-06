# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
​
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        root = TreeNode(preorder.pop(0))
        stack = [root]
        
        while preorder:
            val = preorder.pop(0)
            if val <  stack[-1].val:
                stack[-1].left = TreeNode(val)
                stack.append(stack[-1].left)
            else:
                while stack and val > stack[-1].val:
                    curr_root = stack.pop()
                curr_root.right = TreeNode(val)
                stack.append(curr_root.right)
            
        return root
            
        
        
        
        
                         

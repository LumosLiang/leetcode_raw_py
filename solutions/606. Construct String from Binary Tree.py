# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        
        if t is None: return ""
        
        if not t.left and t.right: return str(t.val) + '()' + '(' + self.tree2str(t.right) + ')'
        elif t.left and not t.right: return str(t.val) + '(' + self.tree2str(t.left)  + ')'
        elif t.left and t.right: return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
        return str(t.val) 
            
​
       
        

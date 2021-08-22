# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        res = []
        
        def helper(root, is_root):
            if not root: return None
            
            isdelete = root.val in to_delete
            
            if is_root and not isdelete: 
                res.append(root)
            root.left = helper(root.left, isdelete)
            root.right = helper(root.right, isdelete)
            return None if isdelete else root 
        
        helper(root, True)
        return res
​
​
    

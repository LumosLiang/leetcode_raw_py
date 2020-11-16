# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
#DFS
​
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        if root is None: return None
        
        node_stack, path_stack, res = [root], [str(root.val)], []
        
        while node_stack:
            temp = node_stack.pop()
            path = path_stack.pop()
            
            if temp.right:
                node_stack.append(temp.right)
                path_stack.append(path + "->" + str(temp.right.val))
            if temp.left:
                node_stack.append(temp.left)
                path_stack.append(path + "->" + str(temp.left.val))
            if temp.right is None and temp.left is None:
                res.append(path)
            
        return res

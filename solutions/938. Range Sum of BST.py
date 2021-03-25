# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
​
        count = 0
        q = []
        q.insert(0, root)
        
        while len(q) != 0:
            temp_node = q.pop()    
            
            if temp_node:
                q.insert(0, temp_node.left)
                q.insert(0, temp_node.right)
​
                if temp_node.val <= R and temp_node.val >= L:
                    count += temp_node.val
        
        return count
            

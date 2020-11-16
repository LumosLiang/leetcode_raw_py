# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        
        ans, q = [], [root]
        
        while q:
            temp_val, temp = [], []
            while q:
                node = q.pop(0)
                temp_val.append(node.val)
                if node.left:
                    temp.append(node.left)                   
                if node.right:
                    temp.append(node.right)
            q = temp
            ans.append(temp_val)
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root is None: return None
        
        res = {root.val:[1]}
        level = 2
        q = [root]
        
        while q:
            temp = []
            sum_val = 0
            while q:
                temp_node = q.pop()
                if temp_node.left:
                    temp.append(temp_node.left)
                    sum_val += temp_node.left.val
                if temp_node.right:
                    temp.append(temp_node.right)
                    sum_val += temp_node.right.val
            if temp != []:
                if sum_val in res:
                    res[sum_val].append(level)
                else:
                    res[sum_val] = [level]
                level += 1
                q = temp
            
        return min(res[max(res)])
                
                
                
        
        

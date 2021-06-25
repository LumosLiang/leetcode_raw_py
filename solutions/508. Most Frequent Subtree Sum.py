# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
     
        hash = {}
        
        def helper(root):
            
            if root is None: return 0
            
            temp = root.val + helper(root.left) + helper(root.right)
            if temp not in hash: hash[temp] = 1
            else: hash[temp] += 1
                
            return temp
            
        helper(root)
        MAX = max(hash.values())
        return [k  for k,v in hash.items() if v == MAX]
        

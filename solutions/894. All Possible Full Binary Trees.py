# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    
    def __init__(self):
         self.memo = {1:[TreeNode(0)]}
    
    def allPossibleFBT(self, N):
        
        if not N % 2: return None 
        
        if N not in self.memo: 
            res = []
            for i in range(1, N, 2):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(N - i - 1):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            self.memo[N] = res
        return self.memo[N]
        
                        
                        
        

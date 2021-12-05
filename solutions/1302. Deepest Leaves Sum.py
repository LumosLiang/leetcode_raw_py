# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
# method1: find the level and level traversal, iterative
# method2: DFS, store the level and value, recursive
​
class Solution:
    def deepestLeavesSum(self, root):
        return self.solution2(root)
    
    def solution1(self, root):
        print(root)
        self.res = []
        
        def helper(root, level):
            if not root: return
            
            if len(self.res) < level + 1:
                self.res.append([])
                
            self.res[level].append(root.val)
                
            helper(root.left, level + 1)
            helper(root.right, level + 1)
        
        helper(root, 0)
        return sum(self.res[-1])
    
    def solution2(self, root):
        
        res = []
        stack = [(root, 0)]
        
        while stack:
            node, level = stack.pop()
            
            if not node: continue
            
            if len(res) < level + 1:
                res.append([])
                
            res[level].append(node.val)
              
            stack.append((node.right, level + 1))
            stack.append((node.left, level + 1))
        
        return sum(res[-1])

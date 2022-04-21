# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # BFS 不要太简单
        
        return self.DFS2(root)
        
        
    def DFS1(self, root):
        # BFS 不要太简单
        
        # DFS, essentially left, right, middle, post-order traversal
        if not root: return []
        
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)
        
        ll, rl = len(left), len(right)
        
        if rl >= ll: return [root.val] + right
        else: return [root.val] + right + left[rl:]
        
    
    def DFS2(self, root):
        
        # root, left, right, pre-order traversal
        
        self.res = []
        
        def helper(root, level):
            
            # base
            if not root: return
            
            if level > len(self.res):
                self.res.append(root.val)
            
            helper(root.right, level + 1)
            helper(root.left, level + 1)
            
        helper(root, 1)
            
        return self.res
            
            
            
            
        
        
        
        
​

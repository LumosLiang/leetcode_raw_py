# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.sol2(root)
        
    # BFS 
    def sol1(self, root):
        if not root: return 0
        
        res = 1
        q = collections.deque([root])
        
        while q:
            temp = collections.deque()
            while q:
                curr = q.popleft()
                if curr.left:
                    temp.append(curr.left)
                if curr.right:
                    temp.append(curr.right)
                if not curr.left and not curr.right:
                    return res
            
            res += 1
            q = temp
            
        return res
    
    # DFS
    def sol2(self, root):
        if not root: return 0
        
        self.res = 10 ** 5 + 1
        
        def helper(root, depth):
            if not root: return depth
            
            if not root.left and not root.right:
                self.res = min(self.res, depth)
            else:
                helper(root.left, depth + 1)
                helper(root.right, depth + 1)
        
        helper(root, 1)
        
        return self.res
        
        
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        # left root right -> preorder, and use two pointer O(N), O(N)
        
        
        # root left right -> inorder, and use hash O(N), O(N + h)
        
        self.set = set()
        
        # under current root, check if a node in this tree is in the set or not.
        
        def traverse(root):
            
            if not root: return False
            
            if root.val in self.set: return True
            
            self.set.add(k - root.val)
            
            return traverse(root.left) or traverse(root.right)
            
        return traverse(root)
    
        # level-order, and use hash O(N), O(N + h)
        
    def sol1(self, root):
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False

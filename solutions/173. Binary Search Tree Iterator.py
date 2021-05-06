# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class BSTIterator:
​
    def __init__(self, root: TreeNode):
        
        self.stack = []
        self.r = root
      
​
    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.r:
            self.stack.append(self.r)
            self.r = self.r.left
        else:
            res = self.stack.pop()
            self.r = res.right
            return res.val
​
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack or self.r is not None
​
            

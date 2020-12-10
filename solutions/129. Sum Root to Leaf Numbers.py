# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        if root is None: return 0
        
        stack, path_stack, paths, res = [root], [[root.val]], [], 0
        
        def process(lst):
            ans = 0
            length = len(lst)
            for i in range(length):
                ans += (10 ** (length - i - 1)) * lst[i]
            return ans
        
        while stack:
            temp = stack.pop()
            path = path_stack.pop()
            
            if temp.right:
                stack.append(temp.right)
                path_stack.append(path + [temp.right.val])
            if temp.left:
                stack.append(temp.left)
                path_stack.append(path + [temp.left.val])
            if temp.right is None and temp.left is None:
                paths.append(path)
        
        for item in paths:
            res += process(item)
        
        return res

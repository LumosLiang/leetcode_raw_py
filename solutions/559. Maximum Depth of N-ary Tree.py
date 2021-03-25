"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# iterative
# BFS
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None: return 0
        
        ans, stack = 0, [root]
        
        while len(stack):
            temp = []
            while len(stack):
                node = stack.pop()
                for child in node.children:
                    temp.append(child)
            stack = temp
            ans += 1
        
        return ans
​
            
        
        
        

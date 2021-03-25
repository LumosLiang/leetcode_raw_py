"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None: return []
        
        ans = []
        
        for child in root.children:
            ans += self.postorder(child)
        
        ans.append(root.val)
        return ans
        
        

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# iterative
DFS
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None: return 
        
        ans, stack = [], [root]
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            
            temp_lst = []
            for child in node.children:
                if child:
                    temp_lst.append(child)
            
            stack += temp_lst[::-1]
            
        return ans    
        
        
        

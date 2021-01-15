"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
​
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return None
        
        stack = [root]
        
        while stack:
            temp = []
            while stack:
                node = stack.pop(0)
                if stack:node.next = stack[0]
                else: node.next = None
                    
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
    
            stack = temp
            
        return root 

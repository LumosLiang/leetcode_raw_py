"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        
        ans, q = [[root.val]], [root]
        
        while q:
            temp_val, temp = [], []
            while q:
                node = q.pop(0)
                for child in node.children:
                    if child:
                        temp.append(child)
                        temp_val.append(child.val)
            if temp_val != []:
                ans.append(temp_val)
            q = temp
        
        return ans 

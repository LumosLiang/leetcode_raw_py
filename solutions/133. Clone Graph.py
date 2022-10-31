"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
​
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
                
        if not node: return 
        
        q = collections.deque([node])
        h = {node: Node(node.val, [])}
        
        while q:
            curr = q.popleft()
            
            for neighbor in curr.neighbors:
                if neighbor not in h:
                    h[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                
                h[curr].neighbors.append(h[neighbor])
        
        return h[node]
            

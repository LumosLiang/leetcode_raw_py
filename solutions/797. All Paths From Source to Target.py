class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
#         dfs/bfs 都可以
#         0 
        
#         0,4   0,3,   0,1
        
#               0,3,4  0,1,3  0,1,2  0,1,4
                     
#                      0,1,3,4   0,1,2,3
                    
#                                0,1,2,3,4
​
        return self.bfs(graph)
​
    def dfs(self, graph):↔​
    
    def bfs(self, graph):
        
        node_q = collections.deque([0])        
        path_q = collections.deque([[0]])
        res = []
        
        while node_q:
            temp_nodes = collections.deque()
            temp_path = collections.deque()
            
            while node_q:
                curr_node = node_q.popleft()
                curr_path = path_q.popleft()
                if curr_node == len(graph) - 1:
                    res.append(curr_path)
                for node in graph[curr_node]:
                    temp_nodes.append(node)
                    temp_path.append(curr_path + [node])
            
            node_q = temp_nodes
            path_q = temp_path
        
        return res
            
            
​
                    
                    
                    
                
        
        
        

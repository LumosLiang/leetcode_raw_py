class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        indegrees, neighbors = self.get_indegree_neighbor(numCourses, prerequisites)
        q = collections.deque([k for k,v in indegrees.items() if v == 0])
        
        while q:
            temp = q.popleft()
            res.append(temp)
            for n in neighbors[temp]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    q.append(n)
              
        return res if len(res) == numCourses else []
    
    def get_indegree_neighbor(self, n, graph):
        count = {node: 0 for node in range(n)}
        neighbor = {node: [] for node in range(n)}
        for pair in graph:
            neighbor[pair[1]].append(pair[0])
            count[pair[0]] += 1
        return count, neighbor
        
        
        

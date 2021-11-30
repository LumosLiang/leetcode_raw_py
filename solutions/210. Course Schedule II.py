class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0 for _ in range(numCourses)]
        point_to_nodes = [[] for _ in range(numCourses)]
        res = []
        
        for pair in prerequisites:
            pre = pair[1]
            curr = pair[0]
            indegree[curr] += 1
            point_to_nodes[pre].append(curr)
            
        q = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        
        while q:
            node = q.popleft()
            res.append(node)
            for ptn in point_to_nodes[node]:
                indegree[ptn] -= 1
                if indegree[ptn] == 0:
                    q.append(ptn)
        
        return res if len(res) == numCourses else []
            
            
        
        
        

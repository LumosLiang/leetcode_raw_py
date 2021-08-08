class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegrees, neighbors = [0] * numCourses, [[] for _ in range(numCourses)]
        for item in prerequisites:
            n, p = item[0], item[1] 
            indegrees[n] += 1
            neighbors[p].append(n)
        
        q = [i for i in range(numCourses) if indegrees[i] == 0]
        
        for i in q:
            for j in neighbors[i]:
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    q.append(j)
              
        return len(q) == numCourses
​
      
        
        
        

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.sol2(numCourses, prerequisites)
    
    # BFS
    # 统计有几个prereq，以及是几个其他node的prereq.
    def sol1(self, numCourses: int, prerequisites: List[List[int]]):
        
        neighbors, preqcnt = [[] for _ in range(numCourses)], [0] * numCourses
        
        # O(N)
        for prereq in prerequisites:
            target, source = prereq[0], prereq[1]
            # compute indegrees
            preqcnt[target] += 1
            
            # compute neighbor
            neighbors[source].append(target)
​
        # O(N)
        q = collections.deque([i for i in range(numCourses) if not preqcnt[i]])
        cnt = len(q)
​
        # BFS O(V + E)
        while q:
            curr = q.popleft()
            for neighbor in neighbors[curr]:
                preqcnt[neighbor] -= 1
                if preqcnt[neighbor] == 0:
                    q.append(neighbor)
                    cnt += 1
​
        # is all zero in all indegree
        return cnt == numCourses
    
    # DFS
    def sol2(self, numCourses: int, prerequisites: List[List[int]]):
        
        neighbors, preqcnt = [[] for _ in range(numCourses)], [0] * numCourses
        
        # O(N)
        for prereq in prerequisites:
            target, source = prereq[0], prereq[1]
            # compute indegrees
            preqcnt[target] += 1
            
            # compute neighbor
            neighbors[source].append(target)
​
        # O(N)
        stack = [i for i in range(numCourses) if not preqcnt[i]]
        cnt = len(stack)
​
        # BFS
        while stack:
            curr = stack.pop()
            for neighbor in neighbors[curr]:
                preqcnt[neighbor] -= 1
                if preqcnt[neighbor] == 0:
                    stack.append(neighbor)
                    cnt += 1
​
        # is all zero in all indegree
        return cnt == numCourses

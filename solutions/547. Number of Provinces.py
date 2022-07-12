        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.cnt -= 1
        
    def find(self, x):
        # base
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # essentially 连通量的问题，和计算岛屿数量是一样的。换了一个样子处理而已
        # BFS/DFS
        
        return self.unionfind(isConnected)
        
    def BFS(self, isConnected):
        # for i in range(n):
        # BFS dq:for every poped node, add all connections itself of this node to dq, mark itself as 0, set the other connection, and 
        # its mirror one to 0
        # cnt + 1 
​
        l = len(isConnected)
        cnt = 0
        
        for i in range(l):
            if isConnected[i][i]:
                q = collections.deque([(i, i)])
                cnt += 1
                
                while q:
                    x, y = q.popleft()
                    for ny in range(y, l):
                        
                        if isConnected[x][ny] == 1:
                            isConnected[x][ny] = 0
                            isConnected[ny][x] = 0
                            isConnected[ny][ny] = 0
                            q.append((ny, x))
        
        return cnt
            
    def DFS(self, isConnected):
        l = len(isConnected)
        cnt = 0
        
        def helper(i, j):
            nonlocal isConnected
            nonlocal l
            
            isConnected[i][j] = 0
            isConnected[j][i] = 0
            isConnected[j][j] = 0
            
            for ny in range(0, l):
                if isConnected[i][ny] == 1:
                    helper(ny, i)
                    
        for i in range(l):
            if isConnected[i][i]:
                cnt += 1
                
                helper(i, i)
        
        return cnt
        
    def unionfind(self, isConnected):
        
        provinces_cnt = len(isConnected)
        uf = UnionFind1(provinces_cnt)
        
        for i in range(provinces_cnt):
            for j in range(i + 1, provinces_cnt):
                if isConnected[i][j]:
                    uf.union(i, j)
        
        return uf.cnt
        
        
        

class UnionFind:↔​
    
class UnionFind1:
    def __init__(self, cnt):
        self.root = [i for i in range(cnt)]
        self.rank = [1 for i in range(cnt)]
        self.cnt = cnt
        
    def union(self, x, y):
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
        
    def BFS(self, isConnected):↔​
            
    def DFS(self, isConnected):↔​
        
    def unionfind(self, isConnected):
        
        provinces_cnt = len(isConnected)
        uf = UnionFind1(provinces_cnt)
        
        for i in range(provinces_cnt):
            for j in range(i + 1, provinces_cnt):
                if isConnected[i][j]:
                    uf.union(i, j)
        
        return uf.cnt
        
        
        

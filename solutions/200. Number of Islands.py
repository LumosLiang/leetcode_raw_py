class UnionFind:
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
    def numIslands(self, grid: List[List[str]]) -> int:
        
        return self.unionfind(grid)
        
    def BFS(self, grid):
        # DFS/BFS都可以
        # 重点是去重？
            # 1. 已经访问过的island，要全部标上
            # 2. 访问的过程中，也要记得标记访问。
        # O(M * N), O(M*N)
        
        # 最坏的情况是所有都是1，bfs的deque的最长的长度是：min(M, N)
        
        res = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    
                    q = collections.deque([[i,j]])
                    grid[i][j] = '0'
                    
                    while q:
                        x,y = q.popleft()    
                        for l, k in [x, y + 1],[x, y - 1],[x - 1, y],[x + 1, y]:
                            if 0 <= l <= m - 1 and 0 <= k <= n - 1 and grid[l][k] == '1':
                                grid[l][k] = '0'
                                q.append([l, k])
                
        return res
    
    def unionfind(self, grid):
        
        cnt = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = cnt
                    cnt += 1
        
        uf = UnionFind(cnt)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "0":
                    master = grid[i][j]
                    for x, y in [i, j + 1],[i, j - 1],[i - 1, j],[i + 1, j]:
                        if 0 <= x <= m - 1 and 0 <= y <= n - 1 and grid[x][y] != "0":
                            neighbor = grid[x][y]
                            uf.union(master, neighbor)
                                
        return uf.cnt
                    
        
    

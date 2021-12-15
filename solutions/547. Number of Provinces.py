class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # DFS & Backtrack
        
        l, w = len(isConnected[0]), len(isConnected)
        
        cnt = 0
        
        for i in range(l):
            for j in range(w):
                if isConnected[i][j] == 1:
                    
                    q = collections.deque([(i, j)])
                    cnt += 1
                    
                    while q:
                        x, y = q.popleft()
                        isConnected[x][y] = 0
                        
                        for ny in range(0, l):
                            if ny == y: continue
                            if isConnected[x][ny] == 1:
                                isConnected[x][ny] = 0
                                if x != ny:
                                    q.append((ny, x))
        
        return cnt

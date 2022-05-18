class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # essentially 连通量的问题，和计算岛屿数量是一样的。换了一个样子处理而已
        # BFS/DFS
        
#         for i in range(n):
    
#             2, BFS dq:
#                 for every poped node, add all connections itself of this node to dq, mark itself as 0, set the other connection, and                      its mirror one to 0
#             3, cnt + 1 
        
        l = len(isConnected)
        cnt = 0
        
        for i in range(l):
            if isConnected[i][i]:
                q = collections.deque([(i, i)])
                cnt += 1
                
                while q:
                    x, y = q.popleft()
                    for ny in range(0, l):
                        if isConnected[x][ny] == 1:
                            isConnected[x][ny] = 0
                            isConnected[ny][x] = 0
                            isConnected[ny][ny] = 0
                            q.append((ny, x))
        
        return cnt
        
        
        

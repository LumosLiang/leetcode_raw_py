class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        m, n = len(image), len(image[0])
        origin_color = image[sr][sc]
        
        visited = [[-1 for i in range(n)] for j in range(m)]
        
        q = collections.deque()
        q.append([sr, sc])
        
        while q:
            i, j = q.popleft()
            image[i][j] = newColor
            visited[i][j] = 0
            
            for x, y in [i + 1, j],[i - 1, j],[i, j + 1],[i, j - 1]:
                if 0 <= x <= m - 1 and 0 <= y <= n - 1 and visited[x][y] != 0 and image[x][y] == origin_color:
                    q.append([x, y])
        
        return image
                
                

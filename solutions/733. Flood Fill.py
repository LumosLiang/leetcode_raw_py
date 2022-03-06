class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # O(MN), O(MN)
        
        m, n = len(image), len(image[0])
        origin_color = image[sr][sc]
        
        # visited = [[-1 for i in range(n)] for j in range(m)]
        
        q = collections.deque([[sr, sc]])
        image[sr][sc] = newColor
        # visited[sr][sc] = 0
        
        if origin_color == newColor: return image
        
        while q:
            i, j = q.popleft()
            
            for x, y in [i + 1, j],[i - 1, j],[i, j + 1],[i, j - 1]:
                if 0 <= x <= m - 1 and 0 <= y <= n - 1 and image[x][y] == origin_color:
                    image[x][y] = newColor
                    # visited[x][y] = 0
                    q.append([x, y])
        
        return image
                
        # basic BFS
        # remember to avoid duplicate: set the newcolor first before entering the q.
        # remember to add visited if some dumplicate cannot be avoid by only comparing val. 
                

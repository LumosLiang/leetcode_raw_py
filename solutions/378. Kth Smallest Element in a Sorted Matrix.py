class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return self.sol2(matrix, k)
        
    # binary seach O(k * log(Diff))
    def sol1(self, matrix: List[List[int]], k: int):
        
        n = len(matrix)
    
        # find the number where there are k elements less or equal than this one
        def less_or_equal(num):
            nonlocal matrix
            nonlocal n
            
            x, y = 0, n - 1
            res = 0
            
            while 0 <= x < n and 0 <= y < n:
                if matrix[x][y] <= num:
                    res += (y + 1)
                    x += 1
                else:
                    y -= 1
​
            return res
        
        left, right = matrix[0][0], matrix[n - 1][n - 1]
        
        while left < right:
            
            mid = (left + right) // 2
            
            curr_cnt = less_or_equal(mid)
    
            if curr_cnt >= k: right = mid
            else: left = mid + 1
​
        return left
    
    # heap
    # typical heap is loop all and pick the top 
    # question now is how we can make use of the sorted matrix
    
    # O(klogK), O(k)
    def sol2(self, matrix: List[List[int]], k: int):
        n = len(matrix)
        heap = [(matrix[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        
        for i in range(k - 1):
            val, x, y = heapq.heappop(heap)
            if x + 1 < n and (x + 1, y) not in visited:
                heapq.heappush(heap, (matrix[x + 1][y], x + 1, y))
                visited.add((x + 1, y))
            if y + 1 < n and (x, y + 1) not in visited:
                heapq.heappush(heap, (matrix[x][y + 1], x, y + 1))
                visited.add((x, y + 1))
        
        return heap[0][0]
            

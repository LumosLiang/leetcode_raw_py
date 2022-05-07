class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return self.sol1(matrix, k)
        
    # binary seach
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
        

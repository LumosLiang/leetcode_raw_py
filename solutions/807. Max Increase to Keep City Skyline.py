class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        res = 0
        right_left = [max(line) for line in grid]
        top_bot = [max([line[i] for line in grid]) for i in range(len(grid[0]))]
        
        for i in range(len(right_left)):
            for j in range(len(top_bot)):
                res += min(right_left[i], top_bot[j]) - grid[i][j]
        return res
        
        

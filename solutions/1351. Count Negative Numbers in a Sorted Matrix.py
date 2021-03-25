class Solution:
    def countNegatives(self, grid):
        count = 0
        for row in grid:
            count += self.binary_search(row)
        return count
​
    def binary_search(self, row):
        low = 0
        high = len(row) - 1
        while low < high:
            mid = low + (high - low) // 2
            if row[mid] < 0:high = mid
            else: low = mid + 1
        if row[low] < 0: return len(row) - low
        else: return 0

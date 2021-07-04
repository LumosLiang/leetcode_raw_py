class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        return max([abs(points[i][0] - points[i + 1][0]) for i in range(len(points) - 1)])

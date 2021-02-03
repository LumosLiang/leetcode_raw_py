class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        vals = [val for row in matrix for val in row]
        heapq.heapify(vals)
        for _ in range(k):
            ans = heapq.heappop(vals)
        return ans

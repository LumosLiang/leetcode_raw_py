class Solution:
    def findKthLargest(self, nums, k):
        import heapq
        heapq.heapify(nums)
        for _ in range(len(nums) - k +1):
            ans = heapq.heappop(nums)
        return ans

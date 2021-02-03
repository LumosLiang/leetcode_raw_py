import heapq
​
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        
        self.res = []
        def backtrack(choice1, choice2, path):
            if path:
                heapq.heappush(self.res, (-sum(path), path))
                if len(self.res) > k:
                    heapq.heappop(self.res)
                return
​
            for i in range(len(choice1)):
                for j in range(len(choice2)):
                    backtrack(choice1, choice2, [choice1[i], choice2[j]])
​
        backtrack(nums1, nums2, [])
        return [r[1] for r in self.res]
​

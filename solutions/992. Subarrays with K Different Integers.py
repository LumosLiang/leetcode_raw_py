class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMost(k):
            start, res = 0, 0
            window = collections.Counter()
            
            for end, val in enumerate(nums):
                window[val] += 1
                while len(window.keys()) > k:
                    window[nums[start]] -= 1
                    if window[nums[start]] == 0: del window[nums[start]]
                    start += 1
                res += end - start + 1
            return res
            
        return atMost(k) - atMost(k - 1)

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        # sliding window
        # +
        # 不符合单调性，你不能随便的shrink window
        # +
        # 加constraint
        # +
        # <= k -> an array where the number of different integers in that array is <= k
        
        # get the number of subarray where the number of different integers in that array is <= k
        def helper(nums, k):
            l = 0
            res = 0
            window = collections.defaultdict(int)
            
            for r, val in enumerate(nums):
                window[val] += 1
                while len(window) > k:
                    window[nums[l]] -= 1
                    if not window[nums[l]]:
                        del window[nums[l]]
                    l += 1
                
                res += r - l + 1
            
            return res
            
        return helper(nums, k) - helper(nums, k - 1)

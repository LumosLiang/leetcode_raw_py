class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # brute force
        res = []
        
        for i in range(len(nums)):
            ans = 0
            for j in range(len(nums)):
                if nums[i] > nums[j] and i != j:
                    ans += 1
            res.append(ans)
        return res

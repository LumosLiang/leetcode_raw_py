class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt=ans=0
        for n in nums:
            cnt=cnt+1 if n else 0
            if cnt>ans: ans=cnt
        return ans

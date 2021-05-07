class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        res = nums
        for i in range(1, l):
            temp = i * [0] + nums[:l - i]
            res = [temp[j] + res[j] for j in range(len(temp))]
            
        return res
    
    
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        pre = nums[0]
        for i in range(1, len(nums)):
            nums[i] += pre
            pre = nums[i]
        
        return nums

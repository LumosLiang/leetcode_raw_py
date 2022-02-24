class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return self.sol2(nums)
        
    def sol1(self, nums):
        p1, p2 = 0, 0
        
        while p2 < len(nums):
            
            if not nums[p2] % 2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1
            
        return nums
    
    def sol2(self, nums):
        p1, p2 = 0, len(nums) - 1
        
        while p1 <= p2:
           
            if not nums[p1] % 2:
                p1 += 1
            elif nums[p2] % 2:
                p2 -= 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 -= 1
                
        return nums

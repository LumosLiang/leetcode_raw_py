class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        lstack, rstack = [], []
        l, r = len(nums) - 1, 0
      
        for i,v in enumerate(nums):
            while lstack and nums[lstack[-1]] > v:
                l = min(l, lstack.pop())
            lstack.append(i)
        
        for j in range(len(nums) - 1, -1, -1):
            while rstack and nums[rstack[-1]] < nums[j]:
                r = max(r, rstack.pop())
            rstack.append(j) 
            
        return r - l + 1 if r - l > 0 else 0
            
        
  
        

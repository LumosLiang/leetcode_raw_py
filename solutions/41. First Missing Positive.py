class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        return self.sol3(nums)
        
    #TLE    
    def sol1(nums):
        m = max(nums)
        
        if m < 0: return 1
        
        for i in range(1, m + 1):
            if i not in nums:
                return i
                
        return m + 1
    
    # Same as other questions
    
    def sol2(self, nums):
        
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                temp = nums[i] - 1
                nums[temp], nums[i] = nums[i], nums[temp]
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] != i:
                return i
        
        return i + 1
            
    def sol3(self, nums):
        nums.append(0)
        n = len(nums)
        
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
                
        print(nums)
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        
        print(nums)
        
        for i in range(1,len(nums)):
            if nums[i]/n==0:
                return i
        return n
                
​

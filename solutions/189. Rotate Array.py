class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.solution3(nums, k)
    
    # in place O(KN), O(1)
    def solution1(self, nums, k):
        cnt = 0
        
        while cnt < k:
            item = nums.pop()
            nums.insert(0,item)   
            cnt += 1
    
    # hash O(N), O(N)
    def solution2(self, nums, k):
        nums_copy, l = copy.deepcopy(nums), len(nums)
        for i in range(len(nums_copy)):
            nums[(i + k) % l] = nums_copy[i]
   
    # two pointers O(N), O(1)
    def solution3(self, nums, k):
        
        def helper(nums, start, end):
            
            if start >= end or start < 0 or end > len(nums) - 1: return
            
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        k = k % len(nums)
        helper(nums, 0, len(nums) - 1)
        helper(nums, 0, k - 1)
        helper(nums, k, len(nums) - 1)
        
            
            
        
    

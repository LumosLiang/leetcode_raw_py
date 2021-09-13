class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums) 
        i, j = l - 2, l - 1 
        
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        
        if i != -1:
            while j <= l - 1:
                if nums[j] > nums[i]:
                    j += 1
                else:
                    nums[j - 1], nums[i] = nums[i], nums[j - 1]
                    break
            if j == l:
                nums[j - 1], nums[i] = nums[i], nums[j - 1]
        
        start, end = i + 1, l - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
​
       
        
        

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # pointers, real deal is p2
        
        
        p1, p2, p3 = 0, len(nums) - 1, len(nums) - 1
        
        while p2 >= p1:
            
            if nums[p2] == 0:
                nums[p2], nums[p1] = nums[p1], nums[p2]
                p1 += 1
            elif nums[p2] == 2:
                nums[p2], nums[p3] = nums[p3], nums[p2]
                p2 -=1
                p3 -= 1
            else:
                p2 -= 1
                
​
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, mid, end = 0, 0, len(nums) - 1
        
        while mid <= end:
            if nums[mid] == 0:
                nums[mid], nums[start] = nums[start], nums[mid]
                start += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
                
        return nums
                
        
        

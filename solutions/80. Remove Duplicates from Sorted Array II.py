class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        slow, fast = 0, 0
        count = 1
        
        while fast < len(nums) - 1:
            if nums[fast] == nums[fast + 1]:
                if count < 2:
                    slow += 1
                    nums[slow] = nums[fast + 1]
                count += 1
            else:
                slow += 1
                nums[slow] = nums[fast + 1]
                count = 1
                          
            fast += 1
        
        return len(nums[:slow + 1])
         

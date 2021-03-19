class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        slow = fast = 0
        
        while fast < len(nums) - 1:
            if nums[fast] != nums[fast + 1]:
                slow += 1
                nums[slow] = nums[fast + 1]
            fast += 1
        return slow + 1

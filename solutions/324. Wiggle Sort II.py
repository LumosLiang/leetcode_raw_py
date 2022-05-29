class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.sol2(nums)
        
    # Greedy + two pointers
    # Wrong! not consider equal.
    def sol1(self, nums):
        new_nums = sorted(nums)
        length = len(nums)
        mid = (length - 1) // 2 
        l, r = mid - 1, mid + 1
        sign = 1
        
        nums[0] = new_nums[mid]
        for i in range(1, length):
            if sign:
                nums[i] == new_nums[r]
                r += 1
            else:
                nums[i] == new_nums[l]
                l -= 1
        
            sign = 1 - sign
        
    def sol2(self, nums):
       
        l = len(nums)
        new_nums = sorted(nums)
        
        mid, r = (l - 1) // 2, l - 1
        
        sign = 1
        for i in range(l):
            if sign:
                nums[i] = new_nums[mid]
                mid -= 1
            else:
                nums[i] = new_nums[r]
                r -= 1
            sign = 1 - sign
        

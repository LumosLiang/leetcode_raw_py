class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Can you do it in O(n) time and/or in-place with O(1) extra space?
        # quick select based on median, and then swap? 
        
        s = copy.deepcopy(nums)
        s.sort()
        
        length = len(nums)
        l, r, p = length // 2 if length % 2 else length // 2 - 1, length - 1, 0
        
        sign = True
        
        while p < length:
​
            if sign:
                nums[p] = s[l]
                l -= 1
            else:
                nums[p] = s[r]
                r -= 1
            sign = not sign
            p += 1
            
                
        # 2,4.1.3.1,3 

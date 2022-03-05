class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.sol1(s)
    
    # O(N), O(1)
    def sol1(self, s):
        l, r = 0, len(s) - 1
        
        while l < r:
            s[l],s[r] = s[r], s[l]
            l += 1
            r -= 1
    
    # O(N), O(1)
    def sol2(self, s):
        
        def helper(nums, left, right):
            if left >= right: return
            
            nums[left], nums[right] = nums[right], nums[left]
            helper(nums, left + 1, right - 1)
        
        helper(s, 0, len(s) - 1)
        
        
        
        
        
        
        

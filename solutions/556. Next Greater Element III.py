class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        # Two pointers + Greedy thinkings? This is really done by myself. Good for me!
        # O(N), O(1)
        
        def rev(nums, l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        nums = list(str(n))
        length = len(nums)
        i, j = length - 2, length - 1
        
        # First search for the first adjacent ones that nums[i] < nums[j]
        while i >= 0 and j >= 1 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
            
        # Then locate i, use j to search for the right side to find the smallest larger one than nums[i]
        # but before that, let's just do a check to see if it is decreasing list, if it is, let's just directly reverse it all
        
        if i == -1: return -1
            
        while j <= length:
            if j == length or nums[j] <= nums[i]: 
                nums[j - 1], nums[i] = nums[i], nums[j - 1]
                break
            j += 1
        
        # reverse the rest after i
        rev(nums, i + 1, length - 1)
        
        res = int("".join(nums))
        return res if res <= 2 ** 31 - 1 else -1

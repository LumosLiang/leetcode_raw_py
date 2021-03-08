class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        
        l = 0
        r = len(height) - 1
        
        while l <= r:
            res = max(res, min(height[l], height[r]) * (r - l))
            
            temp = 0
            if height[l] <= height[r]:
                while l + temp <= r and height[l + temp] <= height[r]:
                    temp += 1
                l += temp
            elif height[l] > height[r]:
                while r - temp >= l and height[r - temp] <= height[l]:
                    temp += 1
                r -= temp
        return res
                

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        
        l = 0
        r = len(height) - 1
        
        while l <= r:
            v = min(height[l], height[r]) * (r - l)
            if v > res: res = v
            # move the curr lower height to a place where first reach the higher height
            temp = 0
            if height[l] <= height[r]:
                while l + temp <= r and height[l + temp] <= height[l]:
                    temp += 1
                l += temp
            elif height[l] > height[r]:
                while r - temp >= l and height[r - temp] <= height[r]:
                    temp += 1
                r -= temp
        return res
                

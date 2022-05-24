class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # 穷举 O(N * N) -> TLE
        
        # area = (i - j) * min(h[i], h[j])
        
        # [1,8,6,2,5,4,8,3,7]
        
        # min(h[i], h[j]) 尽力的去提高这一部分。不用去管结果一定是否高，但是只要有可能我们就去试
        
        # 双指针的做法
        # Greedy
        l, r = 0, len(height) - 1
        res = 0
        
        while l <= r:
            
            min_height = min(height[l], height[r])
            res = max(res, (r - l) * min_height)
            
            # 要去提高的地方在哪一侧
            
            if min_height == height[l]:
                while l + 1 <= r and height[l + 1] < height[l]:
                    l += 1
                l += 1
            else:
                while l <= r - 1 and height[r - 1] < height[r]:
                    r -= 1
                r -= 1
            
        return res

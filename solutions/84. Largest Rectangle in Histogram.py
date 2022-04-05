class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # this is a increase stack, which means that we are finding the next smaller element
        # why next smaller? why increasing stack?
        # 找最大的长方形，观察：
            # 最大的长方形的高度肯定属于这其中一条bar。这里有n种可能的结果，其中一种就是最大的。
            # 找最大的时候怎么找，自然而然的，在每一个bar自己的高度上,看看最远能延伸多远。
            # 向右延伸，如果遇到比自己小的，那就没可能，所以当遇到比自己小的时候，这个bar在向右方向上延伸的长度就到头了。
            # 这时候，就可以算一下向左最远的延伸的长度。
            # 按照这样的想法，组成一个不断递增的栈。每次要弹出的时候，向左看（向栈底看）就可以实现这样的算法：
                # 向左扫，扫到比当前小的位置停止，弹出位置和此时的位置就是这个bar向两边延伸的最长的位置。
        
        
        heights.append(-1)
        stack = [-1]
        res = -1
        
        for right, val in enumerate(heights):
            while heights[stack[-1]] > val:
                h = heights[stack.pop()]
                left = stack[-1]
                w = right - left - 1
                res = max(res, h * w)
            
            stack.append(right)
            
        return res

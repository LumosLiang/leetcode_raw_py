class Solution:
    def nextGreaterElements(self, nums):
        s = []
        size = len(nums)
        res = [-1] * size
​
        for i in range(2 * size - 1, -1, -1):
            while s and s[-1] <= nums[i % size]:
                s.pop()
            if s: res[i % size] = s[-1]
            s.append(nums[i % size])
​
        return res

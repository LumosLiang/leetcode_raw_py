class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
​
        def binary_search(arr, start, end, target):
            if start > end:
                return -1
            mid = start + (end - start) // 2
            if arr[mid] > target:
                return binary_search(arr, start, mid - 1, target)
            if arr[mid] < target:
                return binary_search(arr, mid + 1, end, target)
            return mid
        
        return binary_search(nums, start, end, target)
​

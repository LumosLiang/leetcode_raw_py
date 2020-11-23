class Solution:
    def search(self, nums, target):
         
        def findmin(nums):
            low, high = 0, len(nums) - 1
​
            while (low <= high):
                if low == high:
                    return low
​
                mid = low + (high - low) // 2
                if nums[mid] < nums[mid - 1]:
                    return mid
                else:
                    if nums[mid] > nums[high]:
                        low = mid + 1
                        continue
                    elif nums[mid] < nums[low]:
                        high = mid - 1
                        continue
                    return low
        
        def binary_search(arr, start, end, target):
            if start > end:
                return -1
            mid = start + (end - start) // 2
            if arr[mid] > target:
                return binary_search(arr, start, mid - 1, target)
            if arr[mid] < target:
                return binary_search(arr, mid + 1, end, target)
            return mid
        
        
        min_idx = findmin(nums)
        if target > nums[-1]:
            return binary_search(nums[:min_idx], 0, min_idx - 1 , target)
        else:
            res = binary_search(nums[min_idx:], 0, len(nums) - 1 - min_idx, target)
            if res == -1:
                return res
            else:
                return res+min_idx
​

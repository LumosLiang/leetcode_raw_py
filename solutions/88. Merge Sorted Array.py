class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        m: The number of elements initialized in nums1
        n: The number of elements initialized in nums2
        Do not return anything, modify nums1 in-place instead.
        """
        
        pointer_2 = 0
        pointer_1 = 0
​
        while pointer_2 < n:
            while pointer_1 < len(nums1):
                if nums1[pointer_1] == 0:
                    nums1.insert(pointer_1, nums2[pointer_2])
                    nums1.pop(-1)
                    break
                elif nums2[pointer_2] > nums1[pointer_1]:
                    pointer_1 += 1
                elif nums2[pointer_2] <= nums1[pointer_1]:
                    nums1.insert(pointer_1, nums2[pointer_2])
                    nums1.pop(-1)
                    break
            pointer_2 += 1
        nums1.sort()

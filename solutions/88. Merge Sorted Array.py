class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1, n2, end = m - 1, n - 1, len(nums1) - 1
        
        while n1 >= 0 and n2 >= 0:
            v1, v2 = nums1[n1], nums2[n2]
            if v1 >= v2:
                nums1[end] = v1
                n1 -= 1
            else:
                nums1[end] = v2
                n2 -= 1
            end -= 1
        
        if n1 < 0:
            nums1[:n2+1] = nums2[:n2 + 1]
​

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # phase 1, think of it
            # O(NlogN + MlogM + O(min(M, N))), O(1): two pointers
            # O(N + M), O(N + M): hash
        
        # phase 2, What if the given array is already sorted? How would you optimize your algorithm?
            # no need to sort, directly use two pointers
            # O(min(M, N)), O(1)
            
        # phase 3, What if nums1's size is small compared to nums2's size? Which algorithm is better?
            
            # [1,2,2,4]
            # [1,2,3,5,7,8]
            # binary search
            
        # phase 4, What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
            
            # external sort
            # two pointers
            
        res = []
        i, j = 0, 0
        nums1.sort()
        nums2.sort()
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
                
        return res

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        return set(collections.Counter(nums1).keys()) & set(collections.Counter(nums2).keys())

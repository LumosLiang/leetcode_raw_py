class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = set()
        ans2 = set()
        
        s1, s2 = set(nums1), set(nums2)
        
        for num in nums1:
            if num not in s2:
                ans1.add(num)
        
        for num in nums2:
            if num not in s1:
                ans2.add(num)
        
    
        return [list(ans1), list(ans2)]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # 本质上binary search还是在穷举。。
        # binary search,
        # binary search doing on two
        
        # O(log(m + n)) -> binary search
        # real binary search
        
        l1, l2 = len(nums1), len(nums2)
        lsum = l1 + l2
        if lsum % 2:
            return self.findkth(nums1, nums2, lsum // 2)
        else:
            return (self.findkth(nums1, nums2, lsum // 2) + self.findkth(nums1, nums2, lsum // 2 - 1)) / 2
    
    # the function that can give the kth element from nums1, nums2
    def findkth(self, nums1, nums2, k):
        
        # base
        if not nums1: return nums2[k]
        if not nums2: return nums1[k]
        
        # shrink logic
        
        m1, m2 = len(nums1) // 2, len(nums2) // 2
        
        if m1 + m2 >= k:
            
            # return self.findkth(self, nums1[], nums2[], k - m1//2 - m2//2)
            if nums1[m1] > nums2[m2]:
                return self.findkth(nums1[:m1], nums2, k)
            else:
                return self.findkth(nums1, nums2[:m2], k)
        
        else:
            
            if nums1[m1] > nums2[m2]:
                return self.findkth(nums1, nums2[m2 + 1:], k - m2 - 1)
            else:
                return self.findkth(nums1[m1 + 1:], nums2, k - m1 - 1)
        
    
            # 因为你不知道数据的分布情况。如何判断数据的分布情况？
            # 所以利用中位数的情况来判断，k会落在四个区域的哪个部分？
            # 为什么不是反过来呢？
​
            
​
        
        

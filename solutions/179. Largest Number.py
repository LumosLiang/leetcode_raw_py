class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
    # return a list that has sorted from largest to smallest
        res = self.helper(nums, 0, len(nums) - 1)
        if res == ["0"] * len(res): return "0"
        return "".join(res)
    
    def helper(self, nums, left, right):
        
        if left == right: return [str(nums[left])]
        
        mid = (left + right) // 2
        
        l = self.helper(nums, left, mid)
        r = self.helper(nums, mid + 1, right)
        
        return self.merge(l, r)
    
    def merge(self, A, B):
        
        if not A or not B: return A or B
        
        p1, p2 = 0, 0
        res = []
        
        while p1 < len(A) and p2 < len(B):
            temp = self.compare(A[p1], B[p2])
            if temp:
                res.append(A[p1])
                p1 += 1
            else:
                res.append(B[p2])
                p2 += 1
                
        return res + (B[p2:] if p1 == len(A) else A[p1:])
        
    # return True if nums1 ">" nums2
    def compare(self, nums1, nums2):
        return int(nums1 + nums2) > int(nums2 + nums1)
​
        
        
        
        
        
        
        
        

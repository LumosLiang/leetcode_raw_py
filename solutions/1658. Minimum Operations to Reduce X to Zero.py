class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        ## do two prefix sum for left and right,
        
        if sum(nums) < x: return -1
        
        pf_s_l, pf_s_r, l = [0], [0], len(nums)
        
        for i in range(l):
            pf_s_l.append(pf_s_l[i] + nums[i])
                
        for i in range(l - 1, -1, -1):
            pf_s_r.append(pf_s_r[l - i - 1] + nums[i])
        
        
        ##  since prefix sum, they will be monotonic increasing
        
        res, p = float('inf'), 0
        
        while p < l + 1 and pf_s_l[p] <= x:
            
            temp = self.binarySearch(pf_s_r, x - pf_s_l[p])
            if temp != -1: 
                res = min(res, temp + p)
            p = p + 1
            
        return res if res != float('inf') else -1
        
    def binarySearch(self, nums, target):
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: r = mid - 1
            else: l = mid + 1
            
        return -1
        
        
        
       

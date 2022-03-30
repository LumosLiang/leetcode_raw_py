class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        # pure hash map
        # We must contains all the possibilities
        
        return self.sol2(nums1, nums2, nums3, nums4)
        
    # O(n * n * n)
    def solTLE():
        rest = {}
        length = len(nums1)
        res = 0
        
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    s = nums1[i] + nums2[j] + nums3[k]
                    if -s in rest:
                        rest[-s] += 1
                    else:
                        rest[-s] = 1
        
        for i in range(length):
            if nums4[i] in rest:
                res += rest[nums4[i]]
                
        return res
                
    def sol2(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]):
        rest1, rest2 = {}, {}
        length = len(nums1)
        
        res = 0
        
        for i in range(length):
            for j in range(length):
                s = nums1[i] + nums2[j]
                if -s in rest1:
                    rest1[-s] += 1
                else:
                    rest1[-s] = 1
        
        for i in range(length):
            for j in range(length):
                s = nums3[i] + nums4[j]
                if s in rest2:
                    rest2[s] += 1
                else:
                    rest2[s] = 1
         
        for k1, v1 in rest1.items():
            if k1 in rest2:
                res += v1 * rest2[k1]
                    
        return res
                
                
        

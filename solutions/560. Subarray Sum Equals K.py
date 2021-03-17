class Solution:
    def subarraySum(self, nums, k):
        
        s = res = 0
        hash = {0:1}
​
        for n in nums:
            s += n
            if s - k in hash:
                res += hash[s - k]
            if s in hash:
                hash[s] += 1
            else:
                hash[s] = 1
                
        return res
                

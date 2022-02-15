class Solution:
    def subarraySum(self, nums, k):
        
        prefix_sum = [0]
        
        for i in range(len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i])
        
        hash, res = {k:1}, 0
        
        # hashtable {key, val}
        # key is the relative distance = k, val is the count of relative distance = k
        
        for i in range(1, len(prefix_sum)):
            if prefix_sum[i] in hash:
                res += hash[prefix_sum[i]]
            
            if prefix_sum[i] + k in hash:
                hash[prefix_sum[i] + k] += 1
            else:
                hash[prefix_sum[i] + k] = 1
            
        return res
        
        
        
                

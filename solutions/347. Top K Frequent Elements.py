class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.heap(nums, k)
    
    # O(N + NlogN)
    def hash_sort():
        pass
    
    # O(N + mlogk), O(N)
    def heap(self, nums, k):
        h = collections.Counter(nums)
        freq_idxs = [(v, k) for k, v in h.items()]
        
        res = []
        
        for fi in freq_idxs:
            if len(res) < k:
                heapq.heappush(res, fi)
            else:
                heapq.heappushpop(res, fi)
        
        return [r[1] for r in res]
    
    
#     heappushpop -> 弹出的一定是最小的
#     heapreplace -> 弹出的是上一个定点。
    
    
    # O(N), O(N)
    # guaranteed that the answer is unique
    def quick_select():
        
        return

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # union find/bfs/dfs
        return self.bfs(nums)
        
    def bfs(self, nums):
        
        res = 0
        nums = set(nums)
        
        while nums:
            
            q = collections.deque([nums.pop()])
            cnt = 1
            
            while q:
                curr = q.popleft()
                for nxt in [curr + 1, curr - 1]:
                    if nxt in nums:
                        q.append(nxt)
                        nums.remove(nxt)
                        cnt += 1
            
            res = max(res, cnt)
        
        return res

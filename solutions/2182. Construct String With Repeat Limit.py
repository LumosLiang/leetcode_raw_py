from heapq import heapify, heappop, heappush
​
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        pq = [(-ord(k), v) for k, v in collections.Counter(s).items()]
        heapify(pq)
        res = []
        cnt = 0
        
        while pq:
            max_k, maxk_cnt = heappop(pq)
            
            # if cnt == repeatLimit,
                # if pq is null: break
            
                # pop again
                # and append it
                # push again with update kcnt if kcnt > 0
                # push again maxk, 
                # reset cnt
            
            # if cnt < repeatlimit
            
                # if popkey == res[-1] 
                    # cnt += 1
                    # push again with update kcnt if kcnt > 0
                # else:
                    # push it with update kcnt if kcnt > 0
                    # reset 0
                    # 
                    
            if res and res[-1] == max_k and cnt == repeatLimit:
                if not pq: break
                sec_k, seck_cnt = heappop(pq)
                res.append(sec_k)
                if seck_cnt - 1 > 0: heappush(pq, (sec_k, seck_cnt - 1))
                heappush(pq, (max_k, maxk_cnt))
                cnt = 1
            else:
                if not res or res[-1] != max_k:
                    cnt = 0
                cnt += 1
                res.append(max_k)
                if maxk_cnt - 1 > 0: heappush(pq, (max_k, maxk_cnt - 1))
​
        return "".join([chr(-r) for r in res])
        
        
        

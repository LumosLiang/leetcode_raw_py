class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        return self.heap(times, n, k)
        
    def BFS(self, times: List[List[int]], n: int, k: int):
        
        h = collections.defaultdict(dict)
        
        for time in times:
            u, v, w = time[0], time[1], time[2]
            h[u][v] = w
​
        # use q for dijkstra
        dist = [float('inf')] * n
        dist[k - 1] = 0
        q = collections.deque([k])
        visited = set()
        
        while q:
            curr = q.popleft()
            visited.add(curr)
            mind, minnode = float('inf'), None
            
            for node, w in h[curr].items():
                dist[node - 1] = min(dist[node - 1], dist[curr - 1] + w)
                if node not in visited and dist[node - 1] < mind:
                    mind = dist[node - 1]
                    minnode = node
            if minnode: q.append(minnode)
        
        ans = max([d for d in dist if d != float('inf')])
        return ans if ans != float('inf') else -1
    
    def heap(self, times, n, k):
        
        h = collections.defaultdict(dict)
        
        for time in times:
            u, v, w = time[0], time[1], time[2]
            h[u][v] = w
​
        dist = {}
        heap = [(0, k)]
        
        # while heap:
        #     curr_dis, curr = heapq.heappop(heap)
        #     if curr not in visited:
        #         for node, w in h[curr].items():
        #             if node in dist:
        #                 dist[node] = min(dist[node], curr_dis + w)
        #             else:
        #                 dist[node] = curr_dis + w
        #             heapq.heappush(heap, (dist[node], node))
        #         visited.add(curr)
        
        while heap:
            curr_dis, curr = heapq.heappop(heap)
            if curr not in dist:
                dist[curr] = curr_dis
                for node, w in h[curr].items():
                    heapq.heappush(heap, (w + curr_dis, node))
            
        ans = max(dist.values())
        return ans if len(dist) == n else -1
​

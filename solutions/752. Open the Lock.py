class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        # Each move consists of turning one wheel one slot wrap around +1, -1
        # O(1), O(1)
        
        if target in deadends or "0000" in deadends: return -1
        if target == "0000": return 0
        
        dq = collections.deque(["0000"])
        deadends = set(deadends)
        deadends.add("0000")
        
        res = 1
        
        while dq:
            temp = collections.deque()
            while dq:
                curr_node = dq.popleft()
                for i in range(4):
                    for j in [-1,1]:
                        curr = list(curr_node)
                        if curr[i] == '0' and j == -1:
                            curr[i] = '9' 
                        elif curr[i] == '9' and j == 1:
                            curr[i] = '0'
                        else:
                            curr[i] = str(int(curr[i]) + j)
                        
                        pair = "".join(curr)
                        if pair == target: return res
                        
                        if pair not in deadends:
                            temp.append(pair)
                            deadends.add(pair)
            res += 1
            dq = temp
        
        return -1
        

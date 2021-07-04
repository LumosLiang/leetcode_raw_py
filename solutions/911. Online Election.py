class TopVotedCandidate:
​
    def __init__(self, persons, times):
        self.t, counts self.l = times, collections.Counter(), [persons[0]]
        counts[persons[0]] = 1
        
        for i in range(1, len(self.t)):
            curr = persons[i]
            pre = self.l[i - 1]
            if curr == pre:
                self.l.append(curr)
                counts[curr] += 1
            else:
                counts[curr] += 1
                if counts[curr] >= counts[pre]:
                    self.l.append(curr)
                else:
                    self.l.append(pre)
        
    def q(self, t: int) -> int:
       
        l, r = 0, len(self.t) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if self.t[mid] < t: l = mid + 1
            elif self.t[mid] == t: return self.l[mid]
            else: r = mid - 1
        return self.l[r]
​

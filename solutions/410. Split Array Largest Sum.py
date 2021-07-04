class Solution:
    def splitArray(self, nums, m):
        lo, hi = max(nums), sum(nums)
​
        while lo < hi:
            mid = lo + (hi - lo) // 2
​
            temp, count, total = True, 1, 0
            for n in nums:
                total += n
                if total > mid:
                    count += 1
                    total = n
                    if count > m:
                        temp = False
​
            if temp:
                hi = mid
            else:
                lo = mid + 1
​
        return lo

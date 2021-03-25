class Solution:
    def peakIndexInMountainArray(self, A):
        low = 0
        high = len(A) - 1
        while low < high:
            mid = low + (high - low) // 2
            if A[mid] < A[mid + 1]: low = mid + 1
            elif A[mid] > A[mid + 1]: high = mid
        return low

class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def heappush(self, item):
        self._heap.append(item)
        self._size += 1
        if self._size == 1: return
        self._siftup(self._size - 1)
    
    def _siftup(self, start):
        child = start
        parent = (child - 1) // 2

        while parent >= 0:
            if self._heap[child] < self._heap[parent]:
                self._heap[child], self._heap[parent] = self._heap[parent], self._heap[child]
                child = parent
                parent = (child - 1) // 2
                continue
            break

    def heappop(self):
        if not self._heap: return
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        popitem = self._heap.pop()
        self._size -= 1
        self._siftdown(0)
        return popitem

    def _siftdown(self, start):
        parent = start
        child = 2 * parent + 1
        
        while child < self._size:    
            if child + 1 < self._size and self._heap[child + 1] < self._heap[child]:
                child = child + 1
            if self._heap[parent] > self._heap[child]:
                self._heap[parent], self._heap[child] = self._heap[child], self._heap[parent]
                parent = child
                child = 2 * parent + 1
                continue
            break 
    
    def get_min(self):
        return self._heap[0]

    def get_size(self):
        return self._size

class Solution:
    def findKthLargest(self, nums, k):
        
        return self.sol1(nums, k)
        
    def sol1(self, nums: List[int], k: int) -> int:
        
        # to reduce time complexity, 我们只维护一个k size最大堆
        # 当放入k个数的时候，最顶点就是这些放入的数中，第一大的数。
        # 继续放，
        
        h = Heap()
        
        for num in nums:
            if h.get_size() < len(nums) - k + 1:
                h.heappush(-num)
            else:
                h.heappush(-num)
                h.heappop()
            
        return -h.get_min()
    

    def sol2(self, nums: List[int], k: int) -> int:

        # O(N) random pivot, left, right idx, direct check the k, return None
        def quick_select(nums, left, right, k):
            
            if left >= right: return
            
            pivot_id = (left + right) // 2
            pivot_val = nums[pivot_id]
            
            # put the pivot to the left
            nums[pivot_id], nums[left] = nums[left], nums[pivot_id]
            i = left + 1
            for j in range(i, right + 1):
                if nums[j] < pivot_val:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
                    
            nums[left], nums[i - 1] = nums[i - 1], nums[left]
            
            if k == i - left: return
            
            elif k < i: quick_select(nums, left, i - 2, k) 
            else: quick_select(nums, i, right, k - i + left)
        
        quick_select(nums, 0, len(nums) - 1, len(nums) + 1 - k)
        
        return nums[len(nums) + 1 - k]
    
            
        # follow-up, what if finding the kth smallest?
# def quick_select(nums, left, right, k):
            
#             if left >= right: return
            
#             pivot_id = random.randint(left, right)
#             pivot_val = nums[pivot_id]
            
#             # put the pivot to the left
#             nums[pivot_id], nums[left] = nums[left], nums[pivot_id]
#             i = left + 1
#             for j in range(i, right + 1):
#                 if nums[j] < pivot_val:
#                     nums[j], nums[i] = nums[i], nums[j]
#                     i += 1
                    
#             nums[left], nums[i - 1] = nums[i - 1], nums[left]
            
#             if k == right - (i - 1) + 1: return
#             elif k > right - (i - 1) + 1: quick_select(nums, left, i - 2, k - (right - (i - 1) + 1)) 
#             else: quick_select(nums, i, right, k)
        
#         quick_select(nums, 0, len(nums) - 1, k)
#         return nums[-k]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
​
        # O(N) random pivot, left, right idx, direct check the k
        def quick_select(nums, left, right, k):
            
            if left >= right: return
            
            pivot_id = random.randint(left, right)
            pivot_val = nums[pivot_id]
            
            # put the pivot to the left
            nums[pivot_id], nums[left] = nums[left], nums[pivot_id]
            i = left + 1
            for j in range(i, right + 1):
                if nums[j] < pivot_val:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
                    
            nums[left], nums[i - 1] = nums[i - 1], nums[left]
            
            if k == right - (i - 1) + 1: return
            elif k > right - (i - 1) + 1: quick_select(nums, left, i - 2, k - (right - (i - 1) + 1)) 
            else: quick_select(nums, i, right, k)
        
        quick_select(nums, 0, len(nums) - 1, k)
        return nums[-k]
    
            
        # follow-up, what if finding the kth smallest?
        
​

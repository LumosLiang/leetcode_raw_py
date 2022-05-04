                    r -= 1
            
            helper(nums, left, r)
            helper(nums, l, right)
                    
            
        helper(nums, 0, len(nums) - 1)
        return nums
    
    # O(NlogN), O(logN)
    # quick sort, pivot is the first one.
    def quicksort2(self, nums):
        
        def helper(nums, left, right):
​
            if left >= right: return
            
            pivot_id = left
            pivot_val = nums[pivot_id]
            i = pivot_id + 1
            for j in range(i, right + 1):
                if nums[j] < pivot_val:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
                    
            nums[pivot_id], nums[i - 1] = nums[i - 1], nums[pivot_id]
            
            helper(nums, left, i - 2)
            helper(nums, i, right)
                    
            
        helper(nums, 0, len(nums) - 1)
        return nums
    
    # quick sort, pivot is the random one.
    def quicksort3(self, nums):
        
        def helper(nums, left, right):
​
            if left >= right: return
            
            pivot_id = random.randint(left, right)
            pivot_val = nums[pivot_id]
            nums[left], nums[pivot_id] = nums[pivot_id], nums[left]
            
            i = left + 1
            for j in range(i, right + 1):
                if nums[j] < pivot_val:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
                    
            nums[left], nums[i - 1] = nums[i - 1], nums[left]
            
            helper(nums, left, i - 2)
            helper(nums, i, right)
                    
            
        helper(nums, 0, len(nums) - 1)
        return nums
    
    # quick sort, pivot is the random one, 3 divisions
    def quicksort4(self, nums):
        
        def helper(nums, left, right):
​
            if left >= right: return
            
            pivot_id = random.randint(left, right)
            pivot_val = nums[pivot_id]
            # nums[left], nums[pivot_id] = nums[pivot_id], nums[left]
            
            l, m, r = left, left, right
            
            while m <= r:
                if nums[m] == pivot_val:
                    m += 1
                elif nums[m] < pivot_val:
                    nums[m], nums[l] = nums[l], nums[m]
                    l += 1
                    m += 1
                else:
                    nums[m], nums[r] = nums[r], nums[m]
                    r -= 1
            
            helper(nums, left, l - 1)
            helper(nums, r, right)
                    
            
        helper(nums, 0, len(nums) - 1)
        return nums

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        # compute count of candidate 0s
        
        l, zeroneed = 0, 0
        end = len(arr) - 1
        
        while l < end + 1:
            
            if l + zeroneed > end:
                break
                
            if arr[l] == 0:
                if l + zeroneed == end:
                    arr[-1] = 0
                    end -= 1
                    break
                zeroneed += 1
            
            l += 1
        
        last = end - zeroneed
        
        for i in range(last, - 1, -1):
            
            if arr[i] != 0:
                arr[i + zeroneed] = arr[i]
            else:
                arr[i + zeroneed] = arr[i]
                arr[i + zeroneed - 1] = arr[i]
                zeroneed -= 1
                    
                        
            

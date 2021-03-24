class Solution:
    def numTrees(self, n: int) -> int:
        lst = [i for i in range(1, n + 1)]
        dit = collections.defaultdict(int)
        
        def numOfTrees(lst):
            # give you a inorder list
            # give me how many BSTs it can generate
            
            if not lst: return 1
            
            if not dit[str(lst)]:
                res = 0
                for i in range(len(lst)):
                    res += numOfTrees(lst[:i]) * numOfTrees(lst[i + 1:])  
                dit[str(lst)] = res
                return res
            
            return dit[str(lst)]
​
        return numOfTrees(lst)
                
            
        
        
            
            
        
        
        
        
        
        

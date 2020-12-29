class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        
        def backtrack(choices, path):
            if path:
                res.add(path)
            
            for i in range(len(choices)):
                backtrack(choices[:i] + choices[i + 1:], path + choices[i])
        
        backtrack(tiles, '')
        
        return len(res)
    
​

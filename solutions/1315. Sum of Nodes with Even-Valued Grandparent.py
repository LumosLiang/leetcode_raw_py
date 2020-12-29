class Solution:
    
    def sumEvenGrandparent(self, root):
        
        res = 0
 
        def dfs(root, level):
            nonlocal res
            
            tempLevel = level.copy()
            for i in range(len(tempLevel)):
                tempLevel[i] = tempLevel[i] - 1
                if tempLevel[i] == 0:
                    res += root.val
​
            if 0 in tempLevel:
                tempLevel.remove(0)
​
            if root.val % 2 == 0:
                tempLevel.append(2)
​
            if root.left:
                dfs(root.left, tempLevel)
            if root.right:
                dfs(root.right, tempLevel)
            return res
        
        return dfs(root, [])

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root: return None
        
        res = []
        
        flag = True
        
        dq = collections.deque([root])
        
        while dq:
            temp = collections.deque()
            thisLevel = []
            while dq:
            
                if flag:
                    curr = dq.pop()
                    thisLevel.append(curr.val)
                    if curr.right:
                        temp.appendleft(curr.right)                
                    if curr.left:
                        temp.appendleft(curr.left)
​
                else:
                    curr = dq.popleft()
                    thisLevel.append(curr.val)
                    if curr.left:
                        temp.append(curr.left)                
                    if curr.right:
                        temp.append(curr.right)
                
​
            res.append(thisLevel)
                
            dq = temp
            flag = not flag
​
        
        return res
    
​

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def recoverFromPreorder(self, S):
       
        def recover(S, depth):
            
            if not S: return None
            if len(S) == 1: return TreeNode(S[0])
            
            idx1 = 0
            for i in range(len(S)):
                if S[i] == "-":
                    idx1 = i
                    break
            root = TreeNode(S[0:idx1])
            
            idx2, temp = 0, 0
            for i in range(idx1 + depth, len(S)):
                if S[i] == '-':
                    temp += 1
                else:
                    if temp != 0 and temp == depth:
                        idx2 = i
                        break
                    else:
                        temp = 0
            
            if idx2 != 0:
                root.left = recover(S[depth + idx1: idx2 - depth], depth + 1)
                root.right = recover(S[idx2:], depth + 1)
            else:
                root.left = recover(S[depth + idx1:], depth + 1)
                root.right = recover(None, depth + 1)
            
            return root
        
        return recover(S, 1)
        
        

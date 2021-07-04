# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        
        curr_lev = 0
        
        curr_nodes, curr_nodes_val = [root], [root.val]
        
        
        def check(lst, lev):
            v = lev % 2
            
            if len(lst) == 1 and lst[0] % 2 == v: return False
            
            for i in range(len(lst) - 1):
                if lst[i] % 2 == v or lst[i] >= lst[i + 1]: return False
                
            if lst[-1] % 2 == v: return False
            
            return True
        
        
        while curr_nodes and check(curr_nodes_val, curr_lev):
            nxt_nodes = []
            nxt_nodes_val = []
            while curr_nodes:
                temp = curr_nodes.pop(0)
                if temp.left: 
                    nxt_nodes.append(temp.left)
                    nxt_nodes_val.append(temp.left.val)
                if temp.right: 
                    nxt_nodes.append(temp.right)
                    nxt_nodes_val.append(temp.right.val)
            curr_nodes = nxt_nodes
            curr_nodes_val = nxt_nodes_val
            curr_lev += 1
        else:
            if curr_nodes: return False
        
        return True
                
        
        
        

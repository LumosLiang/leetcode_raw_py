# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        # from descriptions to hashtable
        # hash = node:[leftchild, rightchild, itsparent]
        
        h = {}
       
        for node in descriptions:
            p = node[0]
            if p not in h: h[p] = [0,0,0]
                
            if node[2]:
                h[p][0] = node[1]
            else:
                h[p][1] = node[1]
                
            if node[1] not in h:
                h[node[1]] = [0,0,p]
            else:
                h[node[1]][2] = p
        
        # find root
        r = None
        for k in h:
            if h[k][2] == 0:
                r = k
                break
        
        root = TreeNode(r)
        stack = [root]
        
        while stack:
            curr = stack.pop()
            childs = h[curr.val]
            if childs[0]:
                curr.left = TreeNode(childs[0])
                stack.append(curr.left)
            if childs[1]:
                curr.right = TreeNode(childs[1])
                stack.append(curr.right)
        
        return root
                    
            

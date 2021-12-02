# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # return self.DFS(root, 0)[0]
        return self.BFSLCA(root)
        
    def DFS(self, root, d):
​
        if not root: return [None, d - 1]
​
        if not root.left and not root.right: return [root, d]
​
        [leftlca, ld] = self.DFS(root.left, d + 1)
        [rightlca, rd] = self.DFS(root.right, d + 1)
​
        if ld > rd: return [leftlca, ld]
        elif ld < rd:return [rightlca, rd]
        else: return [root, ld]
    
    def BFSLCA(self, root):
                
        def BFS(root):
            q = collections.deque([root])
            left, right = TreeNode(),TreeNode()
            
            while q:
                temp = collections.deque()
                for i in range(len(q)):
                    node = q[i]
                    if i == 0: left = node
                    if i == len(q) - 1: right = node
                    if node.left: temp.append(node.left)
                    if node.right: temp.append(node.right)
                q = temp
            
            return (left, right)
        
        def LCA(root, node1, node2):
            
            if not root: return None
            
            if root == node1: return node1
            if root == node2: return node2
            
            lLCA = LCA(root.left, node1, node2)
            rLCA = LCA(root.right, node1, node2)
            
            if lLCA and rLCA: return root
            else: return lLCA or rLCA
        
        left, right = BFS(root)
        return LCA(root, left, right)
        
​
        
        
        
        
​
     

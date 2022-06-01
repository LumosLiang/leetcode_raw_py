# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # self.prev = None
        # return self.recursive2(root)
        
        return self.iterative2(root)
            
    # pre-order traversal + foreach
    # O(N), O(N)
    # 最直接的做法
    def iterative1(self, root):
        
        if not root: return None
        
        stack = [root]
        node_list = []
        while stack:
            node = stack.pop()
            node_list.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        for i in range(1, len(node_list)):
            pre, curr = node_list[i - 1], node_list[i]
            pre.left = None
            pre.right = curr

    # pre-order traversal
    # 更 in-place 一点
    # 就像链表操作
    def iterative2(self, root):
        
        if not root: return None
        
        stack = [root]
        dummy = TreeNode()
        pre = dummy
        
        while stack:
            node = stack.pop()
            
            pre.right = node
            pre.left = None
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            pre = node
       
    # post order
    # O(NlogN), O(h) ~ O(N)
    def recursive1(self, root):
        
        if not root: return None
        
        left_list = self.recursive(root.left)
        right_list = self.recursive(root.right)
        
        root.left = None
        root.right = left_list
        curr = root
        
        while curr.right:
            curr = curr.right
        curr.right = right_list
        
        return root 

    # reverse post-order: right -> left -> root
    # 这个比较难理解一点？
    def recursive2(self, root):
        
        if not root: return None
        
        self.recursive2(root.right)
        self.recursive2(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root
        
    
    # morris
    # O(N), O(1)
    def recursive3(self, root):
        
        while root:
            if root.left:
                curr = root.left
                while curr.right:
                    curr = curr.right
                curr.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
    
        
            

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Codec:
​
    def serialize(self, root):
        
        if root is None: return "#,"
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)
        
    def deserialize(self, data):
        
        nodes_lst = data.split(',')
        nodes_lst.pop()
       
        if nodes_lst[0] == '#': return None
        
        root = TreeNode(int(nodes_lst.pop(0)))
        curr = root
        stack = [[root, [0, 1]]]
        
        while nodes_lst:
            node = nodes_lst.pop(0)
            
            while not stack[-1][1]: 
                stack.pop()
            curr = stack[-1][0]
            
            if node != "#":
                if stack[-1][1].pop():
                    curr.left = TreeNode(int(node))
                    curr = curr.left
                else:
                    curr.right = TreeNode(int(node))
                    curr = curr.right
                stack.append((curr, [0, 1]))
            else:
                if stack[-1][1].pop():curr.left = None
                else:curr.right = None          
    
        return root
        
        
​
        
        
        
        
        
​

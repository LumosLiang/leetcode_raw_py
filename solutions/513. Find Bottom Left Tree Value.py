class Solution:
    def findBottomLeftValue(self, root: 'TreeNode') -> 'int':
        
        self.res = 0
        self.pre_height = 0
        
        def helper(root, curr_height):
            if not root: return
            
            if curr_height > self.pre_height:
                self.res = root.val
                self.pre_height = curr_height
                
            helper(root.left, curr_height + 1)
            helper(root.right, curr_height + 1)
        
        helper(root, 1)
  
        return self.res 
​
class Solution:
    def findBottomLeftValue(self, root: 'TreeNode') -> 'int':
        queue = [root]
        while queue:
            node = queue.pop(0)
            res = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return res
​

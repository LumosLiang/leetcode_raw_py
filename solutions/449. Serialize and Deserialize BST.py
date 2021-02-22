# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
# inorder and has to have a placeholder for None
​
class Codec:
​
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None: return ""
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)
        
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        data = data.split(',')
        data.pop()
        
        head = TreeNode(int(data[0]))
        curr = head
        temp = 1
        stack = [curr]
        
        while temp < len(data):
            tmpval = int(data[temp])
            if tmpval < curr.val: 
                curr.left = TreeNode(tmpval)
                curr = curr.left
                stack.append(curr)
                temp += 1
            else:
                while stack and tmpval > stack[-1].val:
                    last_small_node = stack.pop()
                last_small_node.right = TreeNode(tmpval)
                curr = last_small_node.right
                stack.append(curr)
                temp += 1
                
        return head
            
​
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

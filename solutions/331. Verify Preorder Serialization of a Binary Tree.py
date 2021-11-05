class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        if preorder == '#': return True
        
        nodes_lst = preorder.split(',')
        if nodes_lst[0] == '#': return False
        
        root = nodes_lst.pop(0)
        curr = root
        stack = [[root, [0, 1]]]
        
        while nodes_lst:
            node = nodes_lst.pop(0)
            
            while stack and not stack[-1][1]: stack.pop()
            if stack:
                curr = stack[-1][0]
            else:
                return False
            
            if node != "#":
                stack[-1][1].pop()
                curr = node
                stack.append([curr, [0, 1]])
            else:
                stack[-1][1].pop()
        
        if stack[-1][1] == []: return True
        else: return False
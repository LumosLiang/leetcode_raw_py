class Solution:
    def generateTrees(self, n):
        lst = [i for i in range(1, n + 1)]
        dit = collections.defaultdict(list)
        
        def numOfTrees(lst):
            if not lst: return []
            if len(lst) == 1: return [TreeNode(lst[0])]
            
            if not dit[str(lst)]:
                res = []
                for i in range(len(lst)):
                    root_left = numOfTrees(lst[:i])
                    root_right = numOfTrees(lst[i + 1:])
​
                    if not root_left:
                        for right in root_right:
                            root = TreeNode(lst[i])
                            root.right = right
                            res.append(root)
                    elif not root_right:
                        for left in root_left:
                            root = TreeNode(lst[i])
                            root.left = left
                            res.append(root)
                    else:  
                        for left in root_left:
                            for right in root_right:
                                root = TreeNode(lst[i])
                                root.left = left
                                root.right = right
                                res.append(root)
                
                dit[str(lst)] = res
                return res
​
            return dit[str(lst)]
                
        return numOfTrees(lst)

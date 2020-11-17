class Solution:
    def allPathsSourceTarget(self, graph):
        res = []
        
        def backtrack(choices, choice, path):
            if choice == len(choices)-1:
                res.append(path[:])
            
            for i in range(len(choices[choice])):
                backtrack(choices, choices[choice][i], path + [choices[choice][i]])
                
        backtrack(graph, 0, [0])
​
        return res
        
​

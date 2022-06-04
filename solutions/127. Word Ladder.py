class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # Every adjacent pair of words differs by a single letter.
        
        # so the problem is looks like a graph.
        
        # from node beginword to node endword, the shortest length.
        
        # BFS,DFS,DP
        # beginWord = "hit", endWord = "cog", 
        # wordList = ["hot","hig","dig","dot","dog","lot","log","cog"]
        
        # -> {hit:[hot, hig], hot:[dot,lot], hig:[dig], dig:[dog], dot:[dog,lot], dog:[log, cog], lot:[log], log:[cog], cog:[]}
​
# TLE
        # O(beginWord.length)
#         def differ_equal_one(str1, str2):
#             if len(str1) != len(str2): return False
            
#             cnt = 0
#             for i in range(len(str1)):
#                 if str1[i] != str2[i]:
#                     cnt += 1             
#             return cnt == 1
        
#         # generate the graph
#         # O((V + E) * beginWord.length)
#         graph = {beginWord:[]}
#         for word in wordList:
#             graph[word] = []
#             for key in graph:
#                 if differ_equal_one(word, key):
#                     graph[key].append(word)
#                     graph[word].append(key)
        
#         print(graph)
#         # start bfs?
        
        # O(len(wordlist) * beginWord.length * beginWord.length * 26)
        visited = set()
        visited.add(beginWord)
        wordList = set(wordList)
        
        q = collections.deque([beginWord])
        res = 1
        while q:
            temp = collections.deque()
            while q:
​
                curr = q.popleft()
                for i in range(len(curr)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nxt = curr[:i] + c + curr[i + 1:]
                        if nxt in wordList and nxt not in visited:
                            if nxt == endWord: 
                                return res + 1
                            temp.append(nxt)
                            visited.add(nxt)
            q = temp
            res += 1
        
        return 0
​

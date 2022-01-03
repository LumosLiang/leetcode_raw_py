class ListNode:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
​
class LRUCache:
​
    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.table = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
​
    def get(self, key: int) -> int:
        if key in self.table:
            node = self.table[key]
            self._removeFromTable(node)
            self._appendFromHead(node)
            return node.val
        return -1
​
    def put(self, key: int, value: int) -> None:
        
        if key in self.table:
            node = self.table[key]
            self._removeFromTable(node)
        
        node = ListNode(key, value) 
        self._appendFromHead(node)
        self.table[key] = node
        
        if len(self.table) > self.cap:
            popnode = self.tail.prev
            self._removeFromTable(popnode)
            del self.table[popnode.key]
            
    def _removeFromTable(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
​
    def _appendFromHead(self, node):
        Nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = Nxt
        Nxt.prev = node
        
​
​
# # using a dictionary itself
# class LRUCache:
​
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.dic = {}
​
#     def get(self, key: int) -> int:
#         if key in self.dic:
#             val = self.dic.pop(key)
#             self.dic[key] = val
#             return val
#         return -1
        
#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.pop(key)
#             self.dic[key] = value
#         else:
#             if len(self.dic) == self.capacity:
#                 self.dic.pop(next(iter(self.dic)))
#             self.dic[key] = value
​
​

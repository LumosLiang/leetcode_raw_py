# This is to use the 
​
class ListNode:
    def __init__(self, key, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next
​
class MyHashMap:
​
    def __init__(self):
        self.cap = 19997
        self.prime = 12582917
        self.list = [None] * self.cap
        
    def hash(self, key):
        hkey = key * self.prime % self.cap
        return hkey
​
    def put(self, key: int, value: int) -> None:
        
        hkey = self.hash(key)
        
        if not self.list[hkey]:
            self.list[hkey] = ListNode(key, value)
        else:
            pre, curr = None, self.list[hkey]
            while curr:
                if curr.key == key:
                    curr.val = value
                    return
                pre = curr
                curr = curr.next
            pre.next = ListNode(key, value)
​
    def get(self, key: int) -> int:
        
        hkey = self.hash(key)
        
        if self.list[hkey]: 
            curr = self.list[hkey]
            while curr:
                if curr.key == key:
                    return curr.val
                curr = curr.next
        return -1
​
    def remove(self, key: int) -> None:
        
        hkey = self.hash(key)
        
        if self.list[hkey]:
            
            preNode = ListNode(-1)
            preNode.next = self.list[hkey]
            curr = preNode
            
            pre, curr, nxt = None, preNode, None
            
            while curr:
                nxt = curr.next
                if curr.key == key:
                    pre.next = nxt
                    break
                pre = curr
                curr = nxt
            
            self.list[hkey] = preNode.next
​
# class MyHashMap:
​
#     def __init__(self):
#         self.list = [-1] * 1000001
​
#     def put(self, key: int, value: int) -> None:
#         self.list[key] = value
​
#     def get(self, key: int) -> int:
#         return self.list[key]
​
#     def remove(self, key: int) -> None:
#         self.list[key] = -1
​
​
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

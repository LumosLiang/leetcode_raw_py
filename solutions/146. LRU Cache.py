# using a dictionary itself
class LRUCache:
​
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
​
    def get(self, key: int) -> int:
        if key in self.dic:
            val = self.dic.pop(key)
            self.dic[key] = val
            return val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
            self.dic[key] = value
        else:
            if len(self.dic) == self.capacity:
                self.dic.pop(next(iter(self.dic)))
            self.dic[key] = value
​
​
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

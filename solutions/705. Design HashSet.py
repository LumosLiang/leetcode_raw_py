class ListNode:
    def __init__(self, key, next = None):
        self.key = key
        self.next = next
    
class MyHashSet:
 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 1000
        self.prime = 1007
        self.list = [None] * self.cap
        
    def hash(self, key):
        return key * self.prime % self.cap

    def add(self, key: int) -> None:
        
        hkey = self.hash(key)
        
        if not self.list[hkey]: self.list[hkey] = ListNode(key)
        else:
            pre, curr = None, self.list[hkey]
            while curr:
                if curr.key == key:
                    return
                pre = curr
                curr = curr.next
            pre.next = ListNode(key)

    def remove(self, key: int) -> None:
        hkey = self.hash(key)
        
        if self.list[hkey]:
            dummyN = ListNode(-1)
            dummyN.next = self.list[hkey]
            
            pre, curr, nxt = None, dummyN, None
            while curr:
                nxt = curr.next
                if curr.key == key:
                    pre.next = nxt
                    break
                pre = curr
                curr = nxt
            self.list[hkey] = dummyN.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hkey = self.hash(key)
        if self.list[hkey]:
            curr = self.list[hkey]
            while curr:

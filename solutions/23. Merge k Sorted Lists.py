# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # return self.merge_sort(lists, 0, len(lists) - 1)
        
        return self.heap(lists)
        
    # O(logK) * O(n1 + n2)
    def merge_sort(self, lists, l, r):
        
        # base
        if l > r: return None
        if l == r: return lists[l]
        
        mid = (l + r) // 2
        
        left = self.mergeHelper(lists, l, mid)
        right = self.mergeHelper(lists, mid + 1, r)
        
        return self.merge(left, right)
    
    # O(n1 + n2)
    def merge(self, h1, h2):
        
        if not h1 or not h2: return h1 or h2
        
        dummy = ListNode()
        c1, c2, curr = h1, h2, dummy
        
        while c1 and c2:
            if c1.val < c2.val:
                curr.next = c1
                c1 = c1.next
            else:
                curr.next = c2
                c2 = c2.next
            curr = curr.next
            
        curr.next = c1 if c1 else c2
        
        return dummy.next
    
    # [
    #   1->4->5,
    #   1->3->4,
    #   2->6
    # ]
    
    # 需要注意的点是：如何制造唯一性，且能让heap做出比较
    # python中heap的比价逻辑，比0，然后比1，然后比2
    
    def heap(self, lists):
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        dummy = ListNode()
        curr = dummy
        
        while heap:
            val, idx, nxt = heapq.heappop(heap)
            if nxt.next:
                heapq.heappush(heap, (nxt.next.val, idx, nxt.next))
            
            curr.next = nxt
            curr = curr.next
            
        return dummy.next
        
        
        
        
        

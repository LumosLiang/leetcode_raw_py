class Solution:
    def addTwoNumbers(self, l1, l2):
        curr1, curr2 = l1, l2
        len1, len2 = 0, 0
        
        while curr1:
            len1 += 1
            curr1 = curr1.next
        
        while curr2:
            len2 += 1
            curr2 = curr2.next
        
        def add(l1, l2, len1, len2):
        
            curr1, curr2 = l1, l2
            temp = 0
            stack = []
​
            while temp < len1 - len2:
                stack.append(curr1)
                curr1 = curr1.next
                temp += 1
            
            while curr1:
                if curr1.val + curr2.val < 10:
                    curr1.val = curr1.val + curr2.val
                    stack.append(curr1)
                    curr1 = curr1.next
                    curr2 = curr2.next
                else:
                    curr1.val = curr1.val + curr2.val - 10
                    last, temp = 0, [curr1]
                    while stack and stack[-1].val + 1 >= 10:
                        last = stack.pop()
                        last.val += 1 - 10
                        temp.append(last)
                    
                    if stack:
                        stack[-1].val += 1
                    else:
                        l1 = ListNode(1, temp[-1])
                    stack += temp[::-1]
                    
                    curr1 = curr1.next
                    curr2 = curr2.next
            
            return l1
​
        if len1 >= len2:       
            return add(l1, l2, len1, len2)
        else:
            return add(l2, l1, len2, len1)
                      
            
            
            
        

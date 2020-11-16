class Solution:
    def partitionLabels(self, S):
​
        hash = {}
        for k,v in enumerate(S):
            if v not in hash:
                hash[v] = [k]
            else:
                hash[v].append(k)
        
        interval_list = list(hash.values())
        # pointer
        pointer = 0
        while pointer != len(interval_list) - 1:
            # check adjacent two list and see if they overlap
            # or have intersection
            # if yes, expand them, and change the nested list
            # if not, pointer 1 move to next
​
            if interval_list[pointer + 1][0] > interval_list[pointer][-1]:
                pointer += 1
            else:
                interval_list[pointer] += interval_list[pointer + 1]
                interval_list.pop(pointer + 1)
                interval_list[pointer].sort()
        return [len(item) for item in interval_list]
        

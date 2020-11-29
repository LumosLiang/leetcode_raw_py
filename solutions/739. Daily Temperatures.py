class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res, stack = [0] * len(T), []
        pointer = 0
        
        while pointer < len(T):
            while stack and (T[stack[-1]] < T[pointer]):
                idx = stack.pop()
                res[idx] = pointer - idx
            stack.append(pointer)
            pointer += 1
        
        return res
        

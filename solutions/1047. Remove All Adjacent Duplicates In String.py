class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for l in s:
            if stack and stack[-1] == l:
                stack.pop()
            else:
                stack.append(l)
        return "".join(stack)

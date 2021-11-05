class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hash = {'(': ')', '{': '}', '[': ']'}

        for item in s:
            if stack and stack[-1] in hash and hash[stack[-1]] == item:
                stack.pop()
                continue
            stack.append(item)

        return not stack

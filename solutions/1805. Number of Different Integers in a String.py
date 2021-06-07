class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = ''.join([c if '0' <= c <= '9' else ' ' for c in word])
        return len(set([int(n) for n in nums.split()]))
                

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        
        for i in range(len(digits) - 1, -1, -1):
            
            curr = digits[i] + 1
            digits[i] = curr % 10
            carry = curr // 10
            if carry == 0:
                break
​
        if carry:
            return [carry] + digits
        return digits
        
        
            

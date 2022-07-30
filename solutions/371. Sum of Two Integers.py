class Solution:
    def getSum(self, a: int, b: int) -> int:
        
#         0001
#         0010
#         0011
        
#         0001   0001
#         0001   0001
#         0000   0001 (<< 1)
         
       #  1111
       #  1111
       # 11110 = 0000 + 11110
        
        # 不断的查进位，直到没有进位
        mask = 0xffffffff
        base, carry = a& mask, b& mask
        
        while carry:
            
            temp = (carry & base) & mask
            base = (base ^ carry) & mask
            carry = (temp << 1) & mask
            
        if (base>>31) & 1: return ~(base^mask)
        return base
        
    
#     class Solution {
#     public int getSum(int a, int b) {
#       int c; 
#       while(b !=0 ) {
#         c = (a&b);
#         a = a ^ b;
#         b = (c)<<1;
#       }
#       return a;
        
#     }
# }

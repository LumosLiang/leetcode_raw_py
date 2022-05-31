​
public class Solution {
    public int GetSum(int a, int b) {
        
        while(b != 0){
            var carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        
        return a;
    
    }
}
​
        
​
​
​

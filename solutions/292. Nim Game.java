public class Solution {
    public boolean canWinNim(int n) {
        int a = n%4;
        if(a==0){
            return false;
        }
        else{
            return true;
        }
    }
}

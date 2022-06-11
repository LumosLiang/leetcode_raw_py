public class Solution {
    public int MyAtoi(string s) {
        
        // 处理空格
        int i = 0;
        while(i < s.Length && s[i] == ' ')
        {   
            i++;
        }
        if(i >= s.Length) return 0;
        
        // 处理正负号
        int sign = 1;
        if(s[i] == '+' || s[i] == '-')
        {   
            if(s[i] == '-') sign = -1;
            i++;
        }
        if(i >= s.Length) return 0;
        
        // 处理数字
        int res = 0;
        while (i < s.Length && Char.IsDigit(s[i]))
        {
            int r = s[i] - '0';
            if (res > Int32.MaxValue / 10 || res == Int32.MaxValue / 10 && r > 7)
            {
                return sign > 0 ? Int32.MaxValue: Int32.MinValue;
            }
            res = res * 10  + r;
            // if (((next - (s[i] - '0')) / 10) != res)
            // {
            //     return sign > 0 ? Int32.MaxValue: Int32.MinValue;
            // }
            // res = next;
            i++;
        }
        return sign * res;
    }
}


//     def clear(self, s):
        
//         # 处理空格
//         i = 0
//         while i < len(s) and s[i] == " ":
//             i += 1      
//         if i >= len(s): return 0
        
//         # 处理正负号
//         sign = 1
//         if s[i] in ["-","+"]:
//             if s[i] == "-": 
//                 sign = -1
//             i += 1      
//         if i >= len(s): return 0
        
//         # 处理数字
//         res = 0
//         while i < len(s) and ord("0") <= ord(s[i]) <= ord("9"):
//             res = res * 10  + (ord(s[i]) - ord("0"))
//             if (res - (ord(s[i]) - ord("0"))) // 10 != res:
//                 return 
//             i += 1
        
//         # 边界判断 version1
//         if res > 2 ** 31: res = 2 ** 31
//         if sign > 0 and res == 2 ** 31:
//             return (res - 1) * sign
//         return res * sign
        

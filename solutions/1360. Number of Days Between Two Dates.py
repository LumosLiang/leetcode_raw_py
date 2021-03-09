class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = date1.split('-')
        date1 = [int(a) for a in date1]
        date2 = date2.split('-')
        date2 = [int(b) for b in date2]
        
        res = 0
​
        if date1 > date2: date1, date2 = date2, date1
        
        dic = {1:31, 2:[28, 29], 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
​
        while date1 != date2: 
            if date1[0] != date2[0]:
                for i in range(date1[0], date2[0]):
                    if i % 4: res += 365
                    else: res += 366
                
                past = 0
                for j in range(1, date1[1]):
                    if j == 2:
                        if date1[0] % 4:
                            past += dic[j][0]
                        else:
                            if date1[0] % 100:
                                if date1[0] % 400: past += dic[j][1]
                                else: past += dic[j][0]
                            else: past += dic[j][1]
                    else: past += dic[j]
                res -= past + date1[2] - 1
                date1 = [date2[0], 1, 1]
                
            elif date1[1] != date2[1]:
                for k in range(date1[1], date2[1]):
                    if k == 2:
                        if date1[0] % 4:res += dic[k][0]
                        else:
                            if not date1[0] % 100:
                                if not date1[0] % 400: res += dic[k][1]
                                else: res += dic[k][0]
                            else: res += dic[k][1]
                    else: res += dic[k]
                res -= date1[2] - 1
                date1 = [date2[0], date2[1], 1]
                
            elif date1[2] != date2[2]:
                res += date2[2]
                res -= date1[2] 
                date1 = [date2[0], date2[1], date2[2]]
                
        return res
​

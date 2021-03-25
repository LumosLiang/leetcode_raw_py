class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = date1.split('-')
        date1 = [int(a) for a in date1]
        date2 = date2.split('-')
        date2 = [int(b) for b in date2]
        
        res = 0
        if date1 > date2: date1, date2 = date2, date1
        
        dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
​
        while date1 != date2:
            if date1[1] in dic:
                curr_month = dic[date1[1]]
                if date1[1] == 2:
                    if not date1[0] % 4:
                        if not date1[0] % 100:
                            if not date1[0] % 400: curr_month = 29
                        else: curr_month = 29
            else:
                date1[1] = 1
                date1[0] += 1
                date1[2] = 1
            if date1[2] <= curr_month:
                res += 1
                date1[2] += 1
            else:
                if date1[1] <= 12:
                    date1[1] += 1
                    date1[2] = 1                  
        
        return res

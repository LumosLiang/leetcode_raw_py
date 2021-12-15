class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        
        def backtrack(choice, path, cnt):
            # stop condition
            # exactly four and no choice left
            if cnt == 4 and len(choice) == 0:
                res.append(path[:-1])
            
            # loop all choices
            for i in range(len(choice)):
                if self.isValidIP(choice[:i + 1]):
                    backtrack(choice[i + 1:], path + choice[:i + 1] + ".", cnt + 1)
                
        backtrack(s, "", 0)
        
        return res
    
    def isValidIP(self, IP):
        # each integer is between 0 ~ 255 and cannot have leading zeros.
        
        if len(IP) > 4: return False
        
        if len(IP) > 1 and IP[0] == "0": return False
        
        if int(IP) > 255 or int(IP) < 0: return False
        
        return True

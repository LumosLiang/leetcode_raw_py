class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        l = address.split('.')
        
        res = ''
        for s in l:
            res += s + '[.]'
        return res[:len(res) - 3]

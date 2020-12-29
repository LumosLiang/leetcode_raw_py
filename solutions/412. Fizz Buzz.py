class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 != 0:
                res.append(str('Fizz'))
            elif i % 5 == 0 and i % 3 != 0:
                res.append(str('Buzz'))
            elif i % 5 == 0 and i % 3 == 0:
                res.append(str('FizzBuzz'))
            else:
                res.append(str(i))
        return res
            

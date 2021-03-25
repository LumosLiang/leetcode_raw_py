class Solution:
    def canPlaceFlowers(self, flowerbed, n):
​
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            return True if (flowerbed == [0] and n == 1) else False
        
        pointer = 0
        while pointer <= len(flowerbed) - 1:
​
            if pointer == 0:
                if flowerbed[pointer] == 0 and flowerbed[pointer + 1] == 0:
                    flowerbed[pointer] = 1
                    n -= 1
            elif pointer == len(flowerbed) - 1:
                if flowerbed[pointer - 1] == 0 and flowerbed[pointer] == 0:
                    flowerbed[pointer] = 1
                    n -= 1
            elif flowerbed[pointer - 1] == 0 and flowerbed[pointer] == 0 and flowerbed[pointer + 1] == 0:
                flowerbed[pointer] = 1
                n -= 1
            pointer += 1
        
        if n > 0:
            return False
        else:
            return True

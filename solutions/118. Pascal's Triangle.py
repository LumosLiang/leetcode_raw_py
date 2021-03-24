class Solution:
    def generate(self, numRows):
        """
        print function
        """ 
        result = []
        for i in range(numRows):
            result.append(self.getRow(i))

        return result    
    
    def getRow(self, rowIndex):
        """
        Use recursion, but this time move the recursion out of loop
        """
        if rowIndex == 0:
            return [1]
        lst = [1]
        lastrow = self.getRow(rowIndex - 1)
        for i in range(1, rowIndex):
            lst.append(lastrow[i - 1] + lastrow[i])
        lst.append(1)
        return lst

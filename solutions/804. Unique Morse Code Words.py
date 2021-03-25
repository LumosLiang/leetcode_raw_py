class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        moss = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # since all the letter is lower letter, we use ord()
        theset = []
        
        for word in words:
            str1 = ''
            for letter in word:
                index = ord(letter) - ord('a')
                str1 += moss[index]
            if str1 not in theset:    
                theset.append(str1)
        return len(theset)    
        

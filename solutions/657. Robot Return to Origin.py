class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # left x - 1
        # right x + 1
        # up y + 1
        # down y - 1
        
        starting_pos = [0, 0]
        
        for s in moves:
            if s == "U":
                starting_pos[1] += 1
            if s == "D":
                starting_pos[1] -= 1
            if s == "L":
                starting_pos[0] -= 1
            if s == "R":
                starting_pos[0] += 1
        if starting_pos == [0,0]:
            return True
        else:
            return False

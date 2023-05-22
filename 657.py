class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0 # current position on x
        y = 0 # current position on y
        for i in range(len(moves)):
            if(moves[i] == 'U'):
                y += 1
            elif(moves[i] == 'D'):
                y -= 1
            elif(moves[i] == 'L'):
                x -= 1
            else:
                x += 1
        
        if(x == 0 and y == 0):
            return True
        else:
            return False

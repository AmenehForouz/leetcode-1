class Solution:
    def judgeCircle(self, moves: str) -> bool:
        leftRightCount = 0
        upDownCount = 0
        
        for i in moves:
            if i == 'U':
                upDownCount += 1
            elif i == 'D':
                upDownCount -= 1
            elif i == 'L':
                leftRightCount -= 1
            else:
                leftRightCount += 1
        
        if leftRightCount == 0 and upDownCount == 0:
            return True
        else:
            return False
"""
Problem 657 - Robot Return to Origin

There is a robot starting at position (0, 0), the origin, on a 2D plane. Given
a sequence of its moves, judge if this robot ends up at (0, 0) after it 
completes its moves.
"""


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


if __name__ == "__main__":
    print(Solution().judgeCircle('UD')) # Should return True
    print(Solution().judgeCircle('LL')) # Should return False
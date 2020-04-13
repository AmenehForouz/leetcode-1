class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            newint = -1*int(str(-1*x)[::-1])
            if newint < -(2**31):
                return 0
            else:
                return newint
        else:
            newint = int(str(x)[::-1])
            if newint > (2**31 - 1):
                return 0
            else:
                return newint
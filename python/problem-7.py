"""
Problem 7 - Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.
"""

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


if __name__ == "__main__":
    print(Solution().reverse(123)) # Should return 321
    print(Solution().reverse(-123)) # Should return -321
    print(Solution().reverse(120)) # Should return 21
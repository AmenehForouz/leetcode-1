"""
Problem 69 - Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a 
non-negative integer.

Since the return type is an integer, the decimal digits are truncated and 
only the integer part of the result is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            for i in range(x):
                if i * i > x:
                    return i - 1
            return x - 1


if __name__ == "__main__":
    print(Solution().mySqrt(4))  # Return 2
    print(Solution().mySqrt(8))  # Return 2

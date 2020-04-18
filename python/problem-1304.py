"""
Problem 1304 - Find N Unique Integers Sum Up to Zero

Given an integer n, return any array containing n unique integers such that 
they add up to 0.
"""

from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        elif n == 2:
            return [-n, n]
        else:
            sum = 0
            output = [0]*n
            for i in range(len(output) - 1):
                output[i] = -n + i
                sum += (-n + i)
            output[-1] = -sum
            return output


if __name__ == "__main__":
    # Many return possibilities
    print(Solution().sumZero(5))
    print(Solution().sumZero(3))
    print(Solution().sumZero(1))
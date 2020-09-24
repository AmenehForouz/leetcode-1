"""
Problem 1295 - Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even 
number of digits.
"""

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        numEven = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                numEven += 1
        return numEven


if __name__ == "__main__":
    print(Solution().findNumbers([12, 345, 2, 6, 7896]))  # Should return 2
    print(Solution().findNumbers([555, 901, 482, 1771]))  # Should return 1

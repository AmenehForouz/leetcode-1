"""
Problem 977 - Squares of a Sorted Array

Given an array of integers A sorted in non-decreasing order, return an array 
of the squares of each number, also in sorted non-decreasing order.
"""

from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = [i ** 2 for i in A]
        return sorted(A)


if __name__ == "__main__":
    # Should return [0, 1, 9, 16, 100]
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))

    # Should return [4, 9, 9, 49, 121]
    print(Solution().sortedSquares([-7, -3, 2, 3, 11]))

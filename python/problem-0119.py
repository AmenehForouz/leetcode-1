"""
Problem 119 - Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of 
the Pascal's triangle.

Note that the row index starts from 0.
"""

from typing import List


class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            triangle = [[1], [1, 1]]
            for i in range(2, rowIndex + 1):
                triangle.append([1]*(i+1))
                for j in range(1, i):
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle[-1]


if __name__ == '__main__':
    # Should return [1, 3, 3, 1]
    print(Solution().getRow(3))
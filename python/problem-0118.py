"""
Problem 118 - Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's 
triangle.
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            triangle = [[1], [1, 1]]
            for i in range(2, numRows):
                triangle.append([1] * (i + 1))
                for j in range(1, i):
                    triangle[i][j] = (
                        triangle[i - 1][j - 1] + triangle[i - 1][j]
                    )
        return triangle


if __name__ == "__main__":
    # Should return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    print(Solution().generate(5))

"""
Problem 120 - Triangle

Given a triangle, find the minimum path sum from top to bottom. Each 
step you may move to adjacent numbers on the row below.
"""

from typing import List


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], 
                                                      triangle[i+1][j+1])
        return triangle[0][0]


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    
    # Should return 11
    print(Solution().minimumTotal(triangle))
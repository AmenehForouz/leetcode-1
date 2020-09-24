"""
Problem 1252 - Cells with Odd Values in a Matrix

Given n and m which are the dimensions of a matrix initialized by zeros 
and given an array indices where indices[i] = [ri, ci]. For each pair of 
[ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying 
the increment to all indices.
"""

from typing import List
import numpy as np


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = np.zeros(shape=(n, m), dtype=int)
        for i in indices:
            matrix[i[0], :] += 1
            matrix[:, i[1]] += 1
        odd_nums = 0
        for i in matrix:
            for j in i:
                if j % 2 == 1:
                    odd_nums += 1
        return odd_nums


if __name__ == "__main__":
    n = 2
    m = 3
    indices = [[0, 1], [1, 1]]
    # Should return 6
    print(Solution().oddCells(n, m, indices))

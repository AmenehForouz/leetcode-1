"""
Problem 832 - Flipping an Image

Given a binary matrix A, we want to flip the image horizontally, then invert 
it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced 
by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
"""

from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            i.reverse()
            for j in range(len(i)):
                if i[j] == 0:
                    i[j] = 1
                elif i[j] == 1:
                    i[j] = 0
        return A


if __name__ == "__main__":
    img1 = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    img2 = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]

    # Should return [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    print(Solution().flipAndInvertImage(img1))

    # Should return [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
    print(Solution().flipAndInvertImage(img2))

"""
Problem 1299 - Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest 
element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newArray = [0] * len(arr)
        for i in range(1, len(arr)):
            newArray[i - 1] = max(arr[i:])
        newArray[-1] = -1
        return newArray


if __name__ == "__main__":
    # Should return [18, 6, 6, 6, 1, -1]
    print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))

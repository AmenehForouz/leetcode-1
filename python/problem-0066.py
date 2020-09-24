"""
Problem 66

Given a non-empty array of digits representing a non-negative integer, 
plus one to the integer.

The digits are stored such that the most significant digit is at the head 
of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the 
number 0 itself.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_val = "".join([str(i) for i in digits])
        new_val = str(int(new_val) + 1)
        out_digits = []
        for i in new_val:
            out_digits.append(int(i))
        return out_digits


if __name__ == "__main__":
    # Should return [1, 2, 4]
    print(Solution().plusOne([1, 2, 3]))

    # Should return [4, 3, 2, 2]
    print(Solution().plusOne([4, 3, 2, 1]))

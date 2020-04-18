"""
Problem 905 - Sort Array by Parity

Given an array A of non-negative integers, return an array consisting of all 
the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
"""

from typing import List


class Solution:
    
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evenList = []
        oddList = []
        for i in A:
            if i % 2 == 0:
                evenList.append(i)
            else:
                oddList.append(i)
        return evenList + oddList

if __name__ == "__main__":
	# Should return [2, 4, 3, 1]
	print(Solution().sortArrayByParity([3, 1, 2, 4]))
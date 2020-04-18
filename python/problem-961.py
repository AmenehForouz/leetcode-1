"""
Problem 961 - N-Repeated Element in Size 2N Array

In a array A of size 2N, there are N+1 unique elements, and exactly one of 
these elements is repeated N times.

Return the element repeated N times.
"""

from typing import List


class Solution:
   
    def repeatedNTimes(self, A: List[int]) -> int:
        newArray = []
        for i in A:
            if i not in newArray:
                newArray.append(i)
            else:
                return i


if __name__ == "__main__":
	print(Solution().repeatedNTimes([1, 2, 3, 3])) # Should return 3
	print(Solution().repeatedNTimes([2, 1, 2, 5, 3, 2])) # Should return 2

	# Should return 5
	print(Solution().repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))
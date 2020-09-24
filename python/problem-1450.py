"""
Problem 1450 - Number of Students Doing Homework at a Given Time

Given two integer arrays startTime and endTime and given an integer 
queryTime.

The ith student started doing their homework at the time startTime[i] 
and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. 
More formally, return the number of students where queryTime lays in the 
interval [startTime[i], endTime[i]] inclusive.
"""

from typing import List


class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        num_students = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                num_students += 1
        return num_students


if __name__ == "__main__":
    # Should return 1
    print(Solution().busyStudent([1, 2, 3], [3, 2, 7], 4))

    # Should return 1
    print(Solution().busyStudent([4], [4], 4))

    # Should return 0
    print(Solution().busyStudent([4], [4], 5))

    # Should return 0
    print(Solution().busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 7))

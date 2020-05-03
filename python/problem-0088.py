"""
Problem 88 - Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 
as one sorted array.
"""

from typing import List


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            nums1[i+m] = nums2[i]

        nums1.sort()
    

if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    # Should return [1, 2, 2, 3, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)
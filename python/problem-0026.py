"""
Problem 26 - Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each 
element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            temp_index = 0
            length = 1
            for i in range(1, len(nums)):
                if nums[i] != nums[temp_index]:
                    temp_index += 1
                    nums[temp_index] = nums[i]
                    length += 1
        return length


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 2]))  # Should return 2
    # Should return 5
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

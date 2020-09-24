"""
Problem 1389 - Create Target Array in the Given Order

Given two arrays of integers nums and index. Your task is to create target 
array under the following rules:

Initially target array is empty.
- From left to right read nums[i] and index[i], insert at index index[i] the 
  value nums[i] in target array.
- Repeat the previous step until there are no elements to read in nums and 
  index.

Return the target array.
"""

from typing import List


class Solution:
    def createTargetArray(
        self, nums: List[int], index: List[int]
    ) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]

    # Should return [0, 4, 1, 3, 2]
    print(Solution().createTargetArray(nums, index))

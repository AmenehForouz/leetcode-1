"""
Problem 27 - Remove Element

Given an array nums and a value val, remove all instances of that 
value in-place and return the new length.

Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave 
beyond the new length.
"""

from typing import List


class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        else:
            temp_index = 0
            while temp_index < len(nums):
                if nums[temp_index] == val:
                	nums.pop(temp_index)
                else:
                	temp_index += 1
        return len(nums)


if __name__ == "__main__":
	print(Solution().removeElement([3, 2, 2, 3], 3)) # Should return 2
    # Should return 5
	print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
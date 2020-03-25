class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newArray = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    newArray[i] += 1
        return newArray
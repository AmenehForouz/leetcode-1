class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        numEven = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                numEven += 1
        return numEven
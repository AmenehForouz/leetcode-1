class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        newArray = []
        for i in A:
            if i not in newArray:
                newArray.append(i)
            else:
                return i
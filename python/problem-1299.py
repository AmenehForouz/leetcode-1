class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newArray = [0]*len(arr)
        for i in range(1, len(arr)):
            newArray[i-1] = max(arr[i:])
        newArray[-1] = -1
        return newArray
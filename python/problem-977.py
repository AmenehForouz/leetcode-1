class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = [i**2 for i in A]
        return sorted(A)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([i < 0 for sublist in grid for i in sublist])
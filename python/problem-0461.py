"""
Problem 461 - Hamming Distance

Given two integers x and y, calculate the Hamming distance
"""


class Solution:
    
    def hammingDistance(self, x: int, y: int) -> int:
        new_int = x ^ y
        hd = 0
        
        while new_int != 0:
            new_int = new_int & (new_int - 1)
            hd += 1
        
        return hd

if __name__ == "__main__":
    print(Solution().hammingDistance(1, 4)) # Should return 2
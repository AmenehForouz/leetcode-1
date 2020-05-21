"""
Problem 1431 - Kids With the Greatest Number of Candies

Given the array candies and the integer extraCandies, where candies[i] 
represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the 
kids such that he or she can have the greatest number of candies among them. 
Notice that multiple kids can have the greatest number of candies.
"""

from typing import List

class Solution:

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        can_have_most = []
        for kid in candies:
            if kid + extraCandies >= max(candies):
                can_have_most.append(True)
            else:
                can_have_most.append(False)
        return can_have_most
    
if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    # Should return [True, True, True, False, True]
    print(Solution().kidsWithCandies(candies, extraCandies))
"""
Problem 70 - Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can 
you climb to the top?

Note: Given n will be a positive integer.
"""


class Solution:

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            distinct_ways = [0]*n
            distinct_ways[0] = 1
            distinct_ways[1] = 2
            for i in range(2, n):
                distinct_ways[i] = distinct_ways[i-1] + distinct_ways[i-2]
            return distinct_ways[n-1]


if __name__ == '__main__':
    print(Solution().climbStairs(2)) # Return 2
    print(Solution().climbStairs(3)) # Return 3
    print(Solution().climbStairs(4)) # Return 5
"""
Problem 509 - Fibonacci Number

Given N, calculate F(N)
"""


class Solution:

    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return (self.fib(N-1) + self.fib(N-2))

if __name__ == "__main__":
	print(Solution().fib(2)) # Should return 1
	print(Solution().fib(3)) # Should return 2
	print(Solution().fib(4)) # Should return 3
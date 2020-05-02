"""
Problem 709 - To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns 
the same string in lowercase.
"""


class Solution:
    
    def toLowerCase(self, str: str) -> str:
        return str.lower()


if __name__ == "__main__":
	print(Solution().toLowerCase('Hello')) # Should return 'hello'
	print(Solution().toLowerCase('here')) # Should return 'here'
	print(Solution().toLowerCase('LOVELY')) # Should return 'lovely'
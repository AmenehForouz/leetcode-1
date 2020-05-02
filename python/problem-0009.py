"""
Problem 9 - Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when 
it reads the same backward as forward.
"""


class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            if int(str(x)[::-1]) == x:
                return True
            else:
                return False


if __name__ == "__main__":
    print(Solution().isPalindrome(121)) # Should return True
    print(Solution().isPalindrome(-121)) # Should return False
    print(Solution().isPalindrome(10)) # Should return False
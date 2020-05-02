"""
Problem 1281 - Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product 
of its digits and the sum of its digits.
"""


class Solution:
    
    def subtractProductAndSum(self, n: int) -> int:
        sumOfDigits = 0
        prodOfDigits = 1
        
        for i in str(n):
            sumOfDigits += int(i)
            prodOfDigits *= int(i)
        
        return prodOfDigits - sumOfDigits


if __name__ == "__main__":
    print(Solution().subtractProductAndSum(234)) # Should return 15
    print(Solution().subtractProductAndSum(4421)) # Should return 21
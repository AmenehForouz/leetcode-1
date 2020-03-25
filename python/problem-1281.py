class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumOfDigits = 0
        prodOfDigits = 1
        
        for i in str(n):
            sumOfDigits += int(i)
            prodOfDigits *= int(i)
        
        return prodOfDigits - sumOfDigits
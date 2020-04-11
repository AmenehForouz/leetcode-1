class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while True:
            if num == 0:
                return steps
            if num % 2 == 0:
                num /= 2
                steps += 1
            else:
                num -= 1
                steps += 1
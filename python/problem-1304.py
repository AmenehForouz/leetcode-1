class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        elif n == 2:
            return [-n, n]
        else:
            sum = 0
            output = [0]*n
            for i in range(len(output) - 1):
                output[i] = -n + i
                sum += (-n + i)
            output[-1] = -sum
            return output
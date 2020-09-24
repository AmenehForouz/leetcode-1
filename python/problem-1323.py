class Solution:
    def maximum69Number(self, num: int) -> int:
        newNum = list(str(num))
        for i in range(len(newNum)):
            if int(newNum[i]) == 6:
                newNum[i] = "9"
                break
        return int("".join(newNum))

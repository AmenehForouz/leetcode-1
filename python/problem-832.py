class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            i.reverse()
            for j in range(len(i)):
                if i[j] == 0:
                    i[j] = 1
                elif i[j] == 1:
                    i[j] = 0
        return A
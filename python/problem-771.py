class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        total = 0
        
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    total += 1
        
        return total
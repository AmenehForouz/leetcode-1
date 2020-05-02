"""
Problem 771 - Jewels and Stones

You're given strings J representing the types of stones that are jewels, and
S representing the stones you have.  Each character in S is a type of stone 
you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are 
letters. Letters are case sensitive, so "a" is considered a different type of 
stone from "A".
"""


class Solution:
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        total = 0
        
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    total += 1
        
        return total

if __name__ == "__main__":
	print(Solution().numJewelsInStones('aA', 'aAAbbbb')) # Should return 3
	print(Solution().numJewelsInStones('z', 'ZZ')) # Should return 0
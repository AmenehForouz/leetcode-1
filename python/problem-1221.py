"""
Problem 1221 - Split a String in Balanced Strings

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
"""


class Solution:
    
    def balancedStringSplit(self, s: str) -> int:
        L_count = 0
        R_count = 0
        max_strings = 0
        
        for i in range(len(s)):
            
            if s[i] == 'L':
                L_count += 1
            else:
                R_count += 1
                
            if L_count == R_count:
                max_strings += 1
                L_count = 0
                R_count = 0
                
        return max_strings


if __name__ == "__main__":
    print(Solution().balancedStringSplit('RLRRLLRLRL')) # Should return 4
    print(Solution().balancedStringSplit('RLLLLRRRLR')) # Should return 3
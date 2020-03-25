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
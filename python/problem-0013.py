"""
Problem 13 - Roman to Integer

Given a roman numeral, convert it to an integer. Input is guaranteed to be 
within the range from 1 to 3999.
"""


class Solution:
    def romanToInt(self, s: str) -> int:

        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        if len(s) == 1:
            return vals[s[0]]

        converted_int = 0

        i = 0
        while i < len(s):

            if i == len(s) - 1:
                converted_int += vals[s[i]]
                break

            if s[i] == "I":
                if s[i + 1] == "V":
                    converted_int += 4
                    i += 2
                    continue
                elif s[i + 1] == "X":
                    converted_int += 9
                    i += 2
                    continue

            if s[i] == "X":
                if s[i + 1] == "L":
                    converted_int += 40
                    i += 2
                    continue
                if s[i + 1] == "C":
                    converted_int += 90
                    i += 2
                    continue

            if s[i] == "C":
                if s[i + 1] == "D":
                    converted_int += 400
                    i += 2
                    continue
                if s[i + 1] == "M":
                    converted_int += 900
                    i += 2
                    continue

            converted_int += vals[s[i]]
            i += 1

        return converted_int


if __name__ == "__main__":
    print(Solution().romanToInt("III"))  # Should return 3
    print(Solution().romanToInt("IV"))  # Should return 4
    print(Solution().romanToInt("IX"))  # Should return 9
    print(Solution().romanToInt("LVIII"))  # Should return 58
    print(Solution().romanToInt("MCMXCIV"))  # Should return 1994

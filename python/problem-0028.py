"""
Problem 28 - Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if 
needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        else:
            str_arr = haystack.split(needle)
            if len(str_arr) == 1:
                return -1
            else:
                return len(str_arr[0])


if __name__ == "__main__":
    # Should return 2
    print(Solution().strStr("hello", "ll"))

    # Should return -1
    print(Solution().strStr("aaaaa", "bba"))

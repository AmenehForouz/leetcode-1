"""
Problem 20 - Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and 
']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""


class Solution:
    
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        elif len(s) % 2 != 0:
            return False
        else:
            open_brackets = []
            closed_brackets = {'(':')', '[':']', '{':'}'}
            for i in s:
                if i in ['(', '[', '{']:
                    open_brackets.append(i)
                if i in [')', ']', '}']:
                    if len(open_brackets) == 0:
                        return False
                    elif i != closed_brackets[open_brackets.pop(-1)]:
                        return False
            
            if len(open_brackets) > 0:
                return False
            else:
                return True

        
if __name__ == "__main__":
    print(Solution().isValid('()')) # Should return True
    print(Solution().isValid('()[]{}')) # Should return True
    print(Solution().isValid('(]')) # Should return False
    print(Solution().isValid('([)]')) # Should return False
    print(Solution().isValid('{[]}')) # Should return True
    print(Solution().isValid('((')) # Should return False
"""
Problem 1108 - Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""


class Solution:
    
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


if __name__ == "__main__":
    # Should return '1[.]1[.]1[.]1'
    print(Solution().defangIPaddr('1.1.1.1'))

    # Should return '255[.]100[.]50[.]0'
    print(Solution().defangIPaddr('255.100.50.0'))
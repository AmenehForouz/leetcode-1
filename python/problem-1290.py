"""
Problem 1290 - Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of 
each node in the linked list is either 0 or 1. The linked list holds the 
binary representation of a number.

Return the decimal value of the number in the linked list.
"""

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number = str(head.val)
        currNode = head

        while currNode.next != None:
            currNode = currNode.next
            number = number + str(currNode.val)

        power = len(number) - 1
        decNumber = 0

        for i in number:
            decNumber += int(i) * (2 ** power)
            power -= 1

        return decNumber


def list_to_linkedlist(vals: List[int]) -> ListNode:
    head = ListNode(vals[0])
    temp_node = head
    for i in range(1, len(vals)):
        temp_node.next = ListNode(vals[i])
        temp_node = temp_node.next
    return head


if __name__ == "__main__":
    l1 = list_to_linkedlist([1, 0, 1])
    print(Solution().getDecimalValue(l1))  # Should return 5

    l2 = list_to_linkedlist([0])
    print(Solution().getDecimalValue(l2))  # Should return 0

    l3 = list_to_linkedlist([1])
    print(Solution().getDecimalValue(l3))  # Should return 1

    l4 = list_to_linkedlist([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])
    print(Solution().getDecimalValue(l4))  # Should return 18800

    l5 = list_to_linkedlist([0, 0])
    print(Solution().getDecimalValue(l5))  # Should return 0

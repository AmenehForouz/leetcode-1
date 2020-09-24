"""
Problem 2 - Add Two Numbers

You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.
"""

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val1 = []
        val2 = []
        while l1:
            val1.append(str(l1.val))
            l1 = l1.next
        while l2:
            val2.append(str(l2.val))
            l2 = l2.next
        sum_numbers = str(int("".join(val1[::-1])) + int("".join(val2[::-1])))
        head = ListNode(0)
        temp = head
        for i in range(len(sum_numbers) - 1, -1, -1):
            temp.next = ListNode(sum_numbers[i])
            temp = temp.next
        return head.next


def createList(vals: List[int]) -> ListNode:
    head = ListNode(vals[0])
    temp_node = head
    for i in range(1, len(vals)):
        temp_node.next = ListNode(vals[i])
        temp_node = temp_node.next
    return head


def showList(l: ListNode):
    list_string = ""
    while l:
        list_string += str(l.val)
        l = l.next
        if l:
            list_string += " -> "
    return list_string


if __name__ == "__main__":
    l1 = createList([2, 4, 3])
    l2 = createList([5, 6, 4])
    summed_list = Solution().addTwoNumbers(l1, l2)
    print(showList(summed_list))  # Should return '1 -> 1 -> 2 -> 3 -> 4 -> 4'

"""
Problem 24 - Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may 
be changed.
"""

from typing import List


class ListNode:
   
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = ListNode(None)
        new_head.next = head
        temp_1 = new_head
        while temp_1.next and temp_1.next.next:
            temp_2 = temp_1.next
            temp_3 = temp_1.next.next

            temp_1.next = temp_3
            temp_2.next = temp_3.next
            temp_3.next = temp_2

            temp_1 = temp_3.next
        return new_head.next

def createList(vals: List[int]) -> ListNode:
    head = ListNode(vals[0])
    temp_node = head
    for i in range(1, len(vals)):
        temp_node.next = ListNode(vals[i])
        temp_node = temp_node.next
    return head

def showList(l: ListNode):
    list_string = ''
    while l:
        list_string += str(l.val)
        l = l.next
        if l:
            list_string += ' -> '
    return list_string

if __name__ == "__main__":
	l = createList([1, 2, 3, 4])
	# Should return '2 -> 1 -> 4 -> 3'
	print(showList(Solution().swapPairs(l)))
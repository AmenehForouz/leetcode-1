"""
Problem 83 - Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element 
appear only once.
"""

from typing import List


class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        vals = []
        i = head
        while i:
            if i.val not in vals:
                vals.append(i.val)
            i = i.next
        head = ListNode(0, None)
        temp = head
        for i in vals:
            temp.next = ListNode(i, None)
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
    list_string = ''
    while l:
        list_string += str(l.val)
        l = l.next
        if l:
            list_string += ' -> '
    return list_string

if __name__ == '__main__':
    l1 = createList([1, 1, 2])
    l2 = createList([1, 1, 2, 3, 3])

    # Should return 1 -> 2
    print(showList(Solution().deleteDuplicates(l1)))

    # Should return 1 -> 2 -> 3
    print(showList(Solution().deleteDuplicates(l2)))
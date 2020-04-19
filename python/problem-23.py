"""
Problem 23 - Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.
"""

from typing import List


class ListNode:
   
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        values = []
        for i in lists:
            while i:
                values.append(i.val)
                i = i.next
        head = ListNode(None)
        temp_node = head
        for val in sorted(values):
            temp_node.next = ListNode(val)
            temp_node = temp_node.next
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

if __name__ == "__main__":
    l1 = createList([1, 4, 5])
    l2 = createList([1, 3, 4])
    l3 = createList([2, 6])
    # Should return 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
    print(showList(Solution().mergeKLists([l1, l2, l3])))
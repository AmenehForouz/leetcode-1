"""
Problem 21 - Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list 
should be made by splicing together the nodes of the first two lists.
"""

from typing import List


class ListNode:
   
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        
        head = ListNode(None)
        temp_node = head
        while True:
            if l1 and l2:
                if l1.val < l2.val:
                    temp_node.val = l1.val
                    l1 = l1.next
                else:
                    temp_node.val = l2.val
                    l2 = l2.next
            elif l1 and not l2:
                temp_node.val = l1.val
                l1 = l1.next
            elif l2 and not l1:
                temp_node.val = l2.val
                l2 = l2.next
            if not l1 and not l2:
                break
            else:
                temp_node.next = ListNode(None)
                temp_node = temp_node.next
        return head



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
    l1 = createList([1, 2, 4])
    l2 = createList([1, 3, 4])
    merged_list = Solution().mergeTwoLists(l1, l2)
    print(showList(merged_list)) # Should return '1 -> 1 -> 2 -> 3 -> 4 -> 4'
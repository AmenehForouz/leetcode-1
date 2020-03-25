# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
            decNumber += int(i)*(2**power)
            power -= 1

        return decNumber
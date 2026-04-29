# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        #while not on the last node
        while current:
            #go to the following node, store that pointer in temp
            temp = current.next
            #assign the current to the previous value overriding the current value
            current.next = previous
            #set previous to the current value
            previous = current
            #set current to the next value
            current = temp
        return previous


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #need to find length of the linked list
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        toRemove = length - n
        if toRemove == 0:
            return head.next

        cur = head
        for i in range(length-1):
            if (i+1) == toRemove:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
        
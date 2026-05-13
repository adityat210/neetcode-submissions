# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find the length of the list
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        #find the targeted valuue we should skip
        toSkip = length - n

        #skip the first node if that is the node we should skip
        if toSkip == 0:
            head = head.next
            return head

        cur = head
        #any other case, while the current node is valid

        for i in range(length-1):
            if toSkip == (i+1):
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
        




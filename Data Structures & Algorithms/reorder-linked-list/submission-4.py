# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next

        #reverse the second half
        slow.next = None
        prev = None
        while second:
            nxt = second.next #storing the nodes next variable in a temp
            second.next = prev #creating the connection to the previous node
            prev = second #need to update the previous node to the current node
            second = nxt #need to update for the next iteration

        #merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next #need to find the first.next and second.next and store the temps
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2



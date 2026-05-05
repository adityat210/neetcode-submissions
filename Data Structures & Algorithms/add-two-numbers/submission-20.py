# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #need to start the list
        dummy = ListNode()
        cur = dummy

        #need to keep updating the list for all the values in the 2 linked list including the carry
        carry = 0
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            total_val = v1 + v2 + carry
            carry = total_val // 10
            adding_value = total_val % 10
            cur.next = ListNode(adding_value)

            #move the pointers
            if l1: 
                l1 = l1.next 
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else: 
                l2 = None
            cur = cur.next

        return dummy.next
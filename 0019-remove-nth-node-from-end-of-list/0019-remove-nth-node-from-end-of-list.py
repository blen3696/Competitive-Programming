# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        length = 0 
        curr = head

        while curr:
            curr = curr.next
            length += 1

            
        curr = dummy
        idx = 0
        while idx < (length - n):
            curr = curr.next
            idx += 1
        curr.next = curr.next.next

        return dummy.next

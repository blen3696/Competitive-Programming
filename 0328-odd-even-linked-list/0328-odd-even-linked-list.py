# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        o_head = odd
        e_head = even

        curr = head
        idx = 1

        while curr:
            if idx % 2 != 0:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            curr = curr.next
            idx += 1


        odd.next = e_head.next
        even.next = None
    
        return o_head.next
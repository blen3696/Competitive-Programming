# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr = head
        prev = dummy 

        while curr and curr.next:
            if prev.next.val < x:
                prev = prev.next
            if curr.next.val >= x or prev.next.val == curr.next.val:
                curr = curr.next
            else:
               temp = curr.next.next
               curr.next.next = prev.next
               prev.next = curr.next
               curr.next = temp


        return dummy.next 
        
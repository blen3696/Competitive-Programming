# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nth_element(self, curr):
            k = 2
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        
        dummy = ListNode(0,head)
        prev = dummy

        while True:
            nth = self.nth_element(prev) 
            if not nth:
                break
            point = nth.next
            prv,curr = nth.next , prev.next


            while curr and curr != point:
                temp = curr.next
                curr.next = prv
                prv = curr
                curr = temp

            temp = prev.next
            prev.next = nth
            prev = temp

        return dummy.next

        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None 
        curr = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        max_val = float('-inf')

        while prev and curr:
            my_sum = prev.val + curr.val
            max_val = max(max_val, my_sum)

            curr = curr.next
            prev = prev.next

        return max_val
